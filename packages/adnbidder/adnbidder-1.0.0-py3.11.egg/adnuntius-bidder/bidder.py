"""Bidding client for the Adnuntius platform"""

__copyright__ = "Copyright (c) 2023 Adnuntius AS.  All rights reserved."

import signal
import sys
from adnuntius.api import *
from adnuntius.util import date_to_string, str_to_date
from datetime import datetime, timedelta
from threading import Event


class AdnuntiusBidder:
    """
    The main bidder class.
    Custom bidders should inherit from this base, and override methods to provide custom bidding algorithms.
    """

    def __init__(self, api_key, network_id, api_scheme='https', api_host='api.adnuntius.com'):
        """
        Initialises a new bidder.
        :param api_key: Your API key
        :param network_id: The network identifier for your Adnuntius account
        :param api_scheme: https or http
        :param api_host: Hostname for Adnuntius API server
        """
        api_location = api_scheme + '://' + api_host + '/api'
        self.api_client = Api(None, None, api_location, api_key=api_key)
        self.api_client.defaultArgs['context'] = network_id
        self.loop_period = timedelta(minutes=5)
        self.exit = Event()
        for sig in ('TERM', 'HUP', 'INT'):
            signal.signal(getattr(signal, 'SIG' + sig), self.shutdown)

    def start(self):
        """
        Starts the bidding service.
        This runs the main service loop, which periodically fetches the current bidding data for each active line-item
        and makes adjustments to the bid prices as required.
        """
        print('Bidder started!')
        while not self.exit.is_set():
            self.update_all_bids()
            self.call_back()
            self.exit.wait(self.loop_period.total_seconds())
        sys.exit(0)

    def update_all_bids(self):
        """
        Updates the bids for all active Adnuntius line-items.
        This method is a good entry point if the bidder is being run according to an externally controlled schedule,
        for example as a scheduled AWS Lambda.
        - Queries for all active line-items configured for custom bidding control
        - Adjusts the bidding, if required, for each line-item
        :return:
        """
        query_filter = {
            'where': 'biddingAlgorithm=CUSTOM;userState in APPROVED;objectState=ACTIVE;executionState=RUNNING'
        }
        line_items = self.api_client.line_items.query(args=query_filter)
        if len(line_items['results']) == 0:
            print('No custom bidding line-items found')
        else:
            for line_item in line_items['results']:
                print('Updating bids for line-item "' + line_item['name'] + '"')
                self.update_line_item_bids(line_item)

    def update_line_item_bids(self, line_item):
        """
        Updates the bids for a single Adnuntius line-item.
        - Fetches the bidding stats (win-rates, average win/lose CPM, etc)
        - Gets the required updates based upon the bidding stats
        - Sends the updates to Adnuntius
        :param line_item: An Adnuntius line-item
        :return:
        """
        line_item_stats = LineItemBidStats(self.api_client, line_item['id'])
        for bid_update in self.get_line_item_bid_updates(line_item, line_item_stats):
            self.api_client.bidding.update(bid_update)

    def get_line_item_bid_updates(self, line_item, line_item_stats):
        """
        This is the heart of the bidding control algorithm. Custom bidder implementations
        should override this method to provide custom bidding decisions in their adaptor.
        :param line_item: The Line Item object
        :param line_item_stats: The bidding data for the Line Item across all of the Sites where it runs.
        :return: A list of Bid Updates to adjust the bid CPM for the Line Item on specific Sites.
        """
        budget = line_item['objectives']['BUDGET']
        start = str_to_date(line_item['startDate']).replace(tzinfo=None)
        end = str_to_date(line_item['endDate']).replace(tzinfo=None)
        now = datetime.utcnow()
        print(start)
        print(now)
        elapsed_seconds = (now - start).total_seconds()
        remaining_seconds = (end - now).total_seconds()
        print(elapsed_seconds)
        print(remaining_seconds)
        print(budget)
        print('Total Available Impressions Per Second: ' + str(line_item_stats.available_impressions_per_second))
        print('Running on ' + str(len(line_item_stats.site_bids)) + ' sites')
        for site_bid in line_item_stats.site_bids:
            print('\tAdvertiser Site Bidding Win Rates')
            for bid in site_bid.advertiser_site_bids.bid_win_rates:
                print('\t\tBid ' + str(bid))
        return []

    def shutdown(self, sig, frame):
        print('Shutting down bidder...')
        self.exit.set()

    def call_back(self):
        """
        A method stub that can be overridden by child classes.
        This method will be called once per cycle in the main service loop.
        :return:
        """
        return self


class BidWinRate:
    """
    Structure for holding a bid CPM and observed win rate.
    """
    def __init__(self, bid_win_rate):
        self.bid_cpm = bid_win_rate['bidCpm']
        self.win_rate = bid_win_rate['winRate']

    def __str__(self):
        return str(self.bid_cpm['amount']) + ' ' + str(self.win_rate)


class AdvertiserSiteBids:
    """
    Structure for holding the historical win rate, at each CPM price, for an Advertiser on a specific Site.
    This pools data from ALL the Advertiser's line-items.
    - An entry is provided for any CPM bid used in the last 24 hours.
    - At each CPM price, only the most recent 1 hour of bids at that price is used to estimate the expected win rate.
    - The win rate is expressed as a number from 0 to 1, where 0 means the bid always loses and 1 means it always wins.
    """
    def __init__(self, api_client, advertiser_id, site_id):
        """
        Initialise the object
        :param api_client: An initialised Adnuntius API client
        :param advertiser_id: The identifier for the Line Item's Advertiser
        :param site_id: The identifier for the Site
        """
        advertiser_site_bid = api_client.bidding_advertiser_site_stats.get([advertiser_id, site_id])
        self.advertiser_name = advertiser_site_bid['advertiser']['name']
        self.advertiser_id = advertiser_site_bid['advertiser']['id']
        self.site_name = advertiser_site_bid['site']['name']
        self.site_id = advertiser_site_bid['site']['id']
        self.bid_win_rates = [BidWinRate(bid_win_rate) for bid_win_rate in advertiser_site_bid['bids']]


class SiteBidStats:
    """
    Structure for holding bidding data for a Line Item on a specific Site.
    Includes:
    - The total available impressions to bid on during the analysed time-period.
    - The impression share for this Site, expressed as a number from 0 to 1, relative to the total impressions
      available to the Line Item across ALL sites.
    - The win rate, expressed as a number from 0 to 1. A value of 1 means that the Line Item wins every time that
      it submits a bid. A value of 0 means that it never wins.
    - The bidding rate, expressed as a number from 0 to 1. A value lower than 1 means that the line-item delivery
      is being rate controlled by the system and is therefore not bidding on every impression.
    - The average winning bid CPM.
    - The average losing bid CPM.
    - The pooled Advertiser bidding stats for this Site. See
    """
    def __init__(self, api_client, advertiser_id, line_item_site_bids):
        """
        Initialise the object
        :param api_client: An initialised Adnuntius API client
        :param advertiser_id: The identifier for the Line Item's Advertiser
        :param line_item_site_bids: The bidding data from the Adnuntius API.
        """
        self.site_name = line_item_site_bids['site']['name']
        self.site_id = line_item_site_bids['site']['id']
        self.availableImpressions = line_item_site_bids['availableImpressions']
        self.impressionShare = line_item_site_bids['trafficShare']
        self.bidRate = line_item_site_bids['bidRate']
        self.winRate = line_item_site_bids['winRate']
        self.averageWinningCpm = line_item_site_bids['averageWinningCpm']
        self.averageLosingCpm = line_item_site_bids['averageLosingCpm']
        self.advertiser_site_bids = AdvertiserSiteBids(api_client, advertiser_id, self.site_id)


class LineItemBidStats:
    """
    Structure for holding the bidding data for a Line Item.
    Includes:
    - The total available impressions to bid on during the analysed time period (default: the last one hour).
    - The available impressions per second.
    - The bidding data broken down by each Site that the line-item has bid on during the analysed time period.
    """
    def __init__(self, api_client, line_item_id, window=timedelta(hours=1)):
        """
        Initialise the object
        :param api_client: An initialised Adnuntius API client
        :param line_item_id: The identifier for the Line Item
        :param window: The time window to analyse. Default is one hour.
        """
        since = datetime.utcnow() - window
        line_item_stats = api_client.bidding_line_item_stats.get(line_item_id, {'since': date_to_string(since)})
        self.advertiser_name = line_item_stats['advertiser']['name']
        self.advertiser_id = line_item_stats['advertiser']['id']
        self.available_impressions = line_item_stats['availableImpressions']
        range_seconds = line_item_stats['timeRangeSeconds']
        if range_seconds > 0:
            self.available_impressions_per_second = self.available_impressions / range_seconds
        else:
            self.available_impressions_per_second = 0
        self.site_bids = [SiteBidStats(api_client, self.advertiser_id, site_bid) for site_bid in line_item_stats['siteBids']]

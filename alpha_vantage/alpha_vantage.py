#!/usr/bin/env python3

import requests
import pandas as pd
import io
import plotly.express as px


class IntervalOptions:
    one_min = '1min'
    five_min = '5min'
    fifteen_min = '15min'
    thirty_min = '30min'
    sixty_min = '60min'


class SliceOptions:
    year1month1 = "year1month1"
    year1month2 = "year1month2"
    year1month3 = "year1month3"
    year1month4 = "year1month4"
    year1month5 = "year1month5"
    year1month6 = "year1month6"
    year1month7 = "year1month7"
    year1month8 = "year1month8"
    year1month9 = "year1month9"
    year1month10 = "year1month10"
    year1month11 = "year1month11"
    year1month12 = "year1month12"
    yeawr2month1 = "yeawr2month1"
    yeawr2month2 = "yeawr2month2"
    yeawr2month3 = "yeawr2month3"
    yeawr2month4 = "yeawr2month4"
    yeawr2month5 = "yeawr2month5"
    yeawr2month6 = "yeawr2month6"
    yeawr2month7 = "yeawr2month7"
    yeawr2month8 = "yeawr2month8"
    yeawr2month9 = "yeawr2month9"
    yeawr2month10 = "yeawr2month10"
    yeawr2month11 = "yeawr2month11"
    yeawr2month12 = "yeawr2month12"


class OutputSizeOptions:
    compact = 'compact'
    full = 'full'


class AlphaVantage:
    """
    Class to help queerying from alpha vantage
    See: https://www.alphavantage.co/documentation/
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.alpha_vantage_url = 'https://www.alphavantage.co/query'

    def intra_day(self, symbol, interval=IntervalOptions.one_min, adjusted='true', outputsize=OutputSizeOptions.compact,
                  datatype='json'):
        """
        This API returns historical intraday time series for the trailing 2 years,
         covering over 2 million data points per ticker.
        """
        payload = {'function': 'TIME_SERIES_INTRADAY',
                   'symbol': symbol,
                   'interval': interval,
                   'adjusted': adjusted,
                   'outputsize': outputsize,
                   'datatype': datatype,
                   'apikey': self.api_key}
        r = requests.get(url=self.alpha_vantage_url, params=payload)
        ts, meta = r.json()
        df = pd.DataFrame.from_dict(ts, orient='index')
        return df, meta

    def intra_day_extended(self, symbol, slice_option=SliceOptions.year1month1, interval=IntervalOptions.one_min,
                           adjusted='true'):
        """
        This API returns historical intraday time series for the trailing 2 years,
         covering over 2 million data points per ticker.
        """
        payload = {'function': 'TIME_SERIES_INTRADAY_EXTENDED',
                   'symbol': symbol,
                   'interval': interval,
                   'adjusted': adjusted,
                   'slice': slice_option,
                   'apikey': self.api_key}
        r = requests.get(url=self.alpha_vantage_url, params=payload)
        df = pd.read_csv(io.StringIO(r.content.decode('utf-8')))
        return df

    def time_series_daily(self, symbol, outputsize='compact', datatype='json'):
        """
        This API returns raw (as-traded) daily open/high/low/close/volume values, daily adjusted close values,
         and historical split/dividend events of the global equity specified, covering 20+ years of historical data.
        """
        payload = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
                   'symbol': symbol,
                   'outputsize': outputsize,
                   'datatype': datatype,
                   'apikey': self.api_key}
        r = requests.get(url=self.alpha_vantage_url, params=payload)
        json_obj = r.json()
        df = pd.DataFrame.from_dict(json_obj['Time Series (Daily)'], orient='index')
        return df, json_obj['Meta Data']

    def time_series_daily_adj(self, symbol, outputsize='compact', datatype='json'):
        """
        This API returns raw (as-traded) daily open/high/low/close/volume values, daily adjusted close values,
         and historical split/dividend events of the global equity specified, covering 20+ years of historical data.
        """
        payload = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
                   'symbol': symbol,
                   'outputsize': outputsize,
                   'datatype': datatype,
                   'apikey': self.api_key}
        r = requests.get(url=self.alpha_vantage_url, params=payload)
        json_obj = r.json()
        df = pd.DataFrame.from_dict(json_obj['Time Series (Daily)'], orient='index')
        return df, json_obj['Meta Data']

    def quote_endpoint(self, symbol, datatype='json'):
        """
        returns the current price and volume
        """
        payload = {'function': 'GLOBAL_QUOTE',
                   'symbol': symbol,
                   'datatype': datatype,
                   'apikey': self.api_key}
        r = requests.get(url=self.alpha_vantage_url, params=payload)
        return r.json()

    def company_overview(self, symbol):
        """
        returns the current price and volume
        """
        payload = {'function': 'OVERVIEW',
                   'symbol': symbol,
                   'apikey': self.api_key}
        r = requests.get(url=self.alpha_vantage_url, params=payload)
        return r.json()

    @staticmethod
    def plot_timeseries(df):
        """ Plots a timeseries"""
        df['Timestamp'] = df.index
        fig = px.scatter(df, x="Timestamp", y="4. close")
        fig.show()


if __name__ == "__main__":
    alpha_vantage = AlphaVantage(api_key='0ZL19UXID8YMDBDQ')
    ts_df, meta_data = alpha_vantage.time_series_daily(symbol='IBM', outputsize=OutputSizeOptions.full)
    alpha_vantage.plot_timeseries(ts_df)
    # print(alpha_vantage.company_overview('IBM'))
    # res = alpha_vantage.intra_day_extended(symbol='IBM')

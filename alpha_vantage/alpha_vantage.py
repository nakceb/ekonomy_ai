#!/usr/bin/env python3

import requests
import pandas as pd
import plotly.express as px


class IntervalOptions:
    one_min = '1min'
    five_min = '5min'
    fifteen_min = '15min'
    thirty_min = '30min'
    sixty_min = '60min'


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
        return r.json()

    def intra_day_adj(self, symbol, outputsize='compact', datatype='json'):
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
        return r.json()['Time Series (Daily)'], r.json()['Meta Data']

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
    def plot_timeseries(time_series):
        """ Plots a timeseries"""
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df['Timestamp'] = df.index
        fig = px.scatter(df, x="Timestamp", y="4. close")
        fig.show()


if __name__ == "__main__":
    alpha_vantage = AlphaVantage(api_key='0ZL19UXID8YMDBDQ')
    ts, meta = alpha_vantage.intra_day_adj(symbol='IBM', outputsize=OutputSizeOptions.full)
    alpha_vantage.plot_timeseries(ts)
    # print(alpha_vantage.company_overview('IBM'))

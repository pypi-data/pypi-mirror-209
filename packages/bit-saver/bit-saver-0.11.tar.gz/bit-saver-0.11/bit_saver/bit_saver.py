# bit_saver.py

import pyupbit
import pandas as pd
from datetime import datetime, timedelta
import time
import os

class BitSaver:
    """A class to save OHLCV data from Upbit exchange to local storage.
    """
    def __init__(self, save_path='./'):
        """Initializes the BitSaver with a specified save path.

        Args:
            save_path (str): The path where the data will be saved.
        """
        self.save_path = save_path

    def get_start_date(self, ticker, initial_start_date):
        """Get the start date for the specified ticker.

        Args:
            ticker (str): The ticker symbol to get the start date.
            initial_start_date (datetime): The initial start date to begin checking.

        Returns:
            datetime: The start date for the specified ticker.
        """
        while True:
            next_day = initial_start_date + timedelta(days=1)
            df = pyupbit.get_ohlcv(ticker, interval="day", to=next_day)
            if df is None or df.empty:
                initial_start_date += timedelta(days=1)
            else:
                return initial_start_date

    def save_ticker_data(self, ticker, start_date, save_dir):
        """Save OHLCV data for a specific ticker from a specified start date.

        Args:
            ticker (str): The ticker symbol to save data.
            start_date (datetime): The start date from which to begin saving data.
            save_dir (str): The directory in which to save the data.
        """
        dfs = []
        end_date = datetime.now()
        while end_date > start_date:
            df = pyupbit.get_ohlcv(ticker, interval="day", to=end_date)
            if df is None or df.empty:
                break
            dfs.insert(0, df)
            end_date = df.index[0]
            end_date = datetime.strptime(str(end_date), '%Y-%m-%d %H:%M:%S')
        df = pd.concat(dfs)
        df.drop(columns='value', errors='ignore', inplace=True)
        df.to_csv(os.path.join(save_dir, f"{ticker}_ohlcv.csv"))
        print(df)

    def save_all_data(self, save_dir=None):
        """Save OHLCV data for all KRW tickers from Upbit exchange.

        Args:
            save_dir (str): The directory in which to save the data. If None, use the save_path from the constructor.
        """
        if save_dir is None:
            save_dir = self.save_path

        tickers = pyupbit.get_tickers(fiat="KRW")
        initial_start_date = datetime(2017, 9, 24, 9, 0, 0)
        for ticker in tickers:
            print('===========================================')
            print(ticker)
            start_date = self.get_start_date(ticker, initial_start_date)
            print(start_date)
            time.sleep(1)
            self.save_ticker_data(ticker, start_date, save_dir)
            time.sleep(1)

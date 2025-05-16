# run_pipeline.py

from data.data_loader import download_full_data_for_each_ticker
import pandas as pd


tickers = ["AAPL", "MSFT", "GOOG", "META", "TSLA"]
download_full_data_for_each_ticker(tickers, start="2020-01-01", end="2023-10-01", save_path="/Users/xhma/Code/Quant_Projects/quant_factor_project/data/")
import yfinance as yf
import pandas as pd
import os

def download_price_data(tickers,
    start,
    end,
    field,
    save_path):

    all_data = {}

    for ticker in tickers:
        try:
            df = yf.download(ticker, start=start, end=end)
            all_data[ticker] = df[field]
            print(f"[✓] {ticker} downloaded successfully.")
        except Exception as e:
            print(f"[✗] Failed to download {ticker}: {e}")

    price_df = pd.DataFrame(all_data)
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        price_df.to_csv(save_path)
        print(f"Data saved to {save_path}")

    return price_df

def download_full_data_for_each_ticker(tickers, start, end, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    for ticker in tickers:
        try:
            df = yf.download(ticker, start=start, end=end)
            filepath = os.path.join(save_path, f"{ticker}.csv")
            df.to_csv(filepath)
            print(f"[✓] {ticker} saved to {filepath}")
        except Exception as e:
            print(f"[✗] Failed to download {ticker}: {e}")

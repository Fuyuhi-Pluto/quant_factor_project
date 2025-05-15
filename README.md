# Quant Factor Research Project

This project explores the construction and evaluation of alpha factors for equity strategies using open financial data.

## 🔍 Project Objective

- Build, test, and validate stock selection factors (e.g., momentum, volatility, value)
- Analyze their predictive power via Information Coefficient (IC)
- Simulate portfolio returns using simple backtest

## 🗂 Project Structure

quant_factor_project/
├── data/ # Raw price/fundamental data
├── factors/ # Factor scripts (e.g., momentum.py, volatility.py)
├── analysis/ # IC calculation and visualizations
├── backtest/ # Backtest scripts for top-N selection
├── notebook/ # Jupyter notebook demos
└── README.md # This file


## 🧠 Example Factors

- **Momentum:** Past 60-day return
- **Volatility:** 20-day rolling std of returns
- **Value:** Inverse PE ratio (when available)

## 📦 Tech Stack

- Python, Pandas, yfinance
- Matplotlib / Seaborn
- Optional: bt / Backtrader for backtesting

## 🚀 How to Use

1. Run `data/data_loader.py` to download stock price data
2. Use `factors/momentum.py` to compute factor values
3. Use `analysis/ic_analysis.py` to evaluate IC
4. Run `backtest/simple_backtest.py` to simulate top-N strategy
5. See results in `notebook/factor_pipeline_demo.ipynb`

## 🧩 Future Enhancements

- Add more fundamental factors (e.g., ROE, FCF yield)
- Implement multi-factor scoring & weighting
- Add transaction cost model in backtest


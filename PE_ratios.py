#Learning to import data from libraries 
#pip install yfinance
#https://pypi.org/project/yfinance/ 

import yfinance as yf

# List of stock tickers in Semiconductor sector
tickers = ["NVDA", "AMD", "INTC", "ASML", "MU", "QCOM", "AVGO"]

for i in tickers:
    stock = yf.Ticker(i)
    info = stock.info
    print(f"{i} - P/E Ratio: {info.get('trailingPE', 'N/A')}, Forward P/E Ratio: {info.get('forwardPE', 'N/A')}")
    

#Learning to import data from libraries 
#pip install yfinance
#https://pypi.org/project/yfinance/ 

import yfinance as yf

nvda = yf.Ticker("NVDA")
info = nvda.info 
#.info this is where it goes to the internet and grabs a big pile of data 
#.info  is a dictionary containing various information about the stock
print(f"Trailing PE: {info['trailingPE']}")
print(f"Forward PE: {info['forwardPE']}")

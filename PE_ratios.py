#Learning to import data from libraries 
#pip install yfinance
#https://pypi.org/project/yfinance/ 

import yfinance as yf


print(f"Trailing PE: {info['trailingPE']}")
print(f"Forward PE: {info['forwardPE']}")
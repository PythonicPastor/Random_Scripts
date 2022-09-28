
# Raw Package 
import numpy as np 
import pandas as pd
from pandas_datareader import data as pdr 
import os
# Market Data 
import yfinance as yf

# Visualization
import matplotlib.pyplot as plt


#Code
yf.pdr_override()
df = yf.download(tickers='WMT',period='1d',interval='5m')
print(df.index)
plt.plot(df.index,df['Adj Close'], color = 'red')
plt.xticks(rotation=45)
plt.title("Walmart Stocks")
plt.show()
    

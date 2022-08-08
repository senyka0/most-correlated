import ccxt 
import numpy as np 
import pandas as pd
exchange = ccxt.binanceusdm()
markets = [i["id"] for i in exchange.fetch_markets() if i["id"][-4:] == "USDT"]
all = {}
for symbol in markets:
        prices = [i[1] for i in exchange.fetch_ohlcv(symbol, '1h')][-168:]
        changes = np.diff(prices)/prices[:-1]*100
        all[symbol] = changes
df = pd.DataFrame(all)
corr = df.corr()
print(corr.where(np.triu(np.ones(corr.shape), 1).astype(np.bool)).unstack().dropna().sort_values().tail(50)) #print 50 the most positive correlated coins

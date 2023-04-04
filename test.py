import yfinance as yf
import pandas_ta as ta

# Get stock data using yfinance
df = yf.download('KOTAKBANK.BO', period = '2mo')

# Calculate MACD using ta
# macd_df = ta.macd(stock_data['Close'])
# mac = stock_data.ta.macd(close='Close', fast=12, slow=26, signal=9, append=True)
#12 day ema
k = df['Close'].ewm(span=12, adjust=False, min_periods=12).mean()
#26 day ema
d = df['Close'].ewm(span=26, adjust=False, min_periods=26).mean()

macd = k -d
# Get the 9-Day EMA of the MACD for the Trigger line
macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()

# Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
macd_h = macd - macd_s

# Add all of our new values for the MACD to the dataframe
df['macd'] = df.index.map(macd)
df['macd_h'] = df.index.map(macd_h)
df['macd_s'] = df.index.map(macd_s)
print(df)
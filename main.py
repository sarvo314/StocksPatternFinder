import yfinance as yf
import mplfinance as mpf
import pandas_ta as ta
# from pyti.macd import macd
# import talib
# Define a function to check if a stock has a previous downtrend and a hammer candlestick
def has_previous_downtrend_and_hammer(ticker_symbol):
	# Download historical data for the stock
	stock_data = yf.download(ticker_symbol, period='1mo')
	# print(stock_data)

	# Check if the latest candlestick is a hammer
	last_candle = stock_data.iloc[-1]
	# print(last_candle)
	body_size = abs(last_candle['Open'] - last_candle['Close'])
	lower_shadow_size = last_candle['Low'] - min(last_candle['Open'], last_candle['Close'])
	upper_shadow_size = max(last_candle['Open'], last_candle['Close']) - last_candle['High']
	# is_hammer = body_size < lower_shadow_size and body_size < upper_shadow_size and last_candle['Close'] > last_candle['Open']
	is_hammer = lower_shadow_size > 1.8 * body_size and upper_shadow_size < body_size
	# Check if the stock has a previous downtrend
	# if is_hammer:
	print(stock_data['Close'])
	print(ta.macd(stock_data['Close']))
	# my_df = macd_df['macd']
	# print(macd["macd"])
	# print(my_df)
	# signal_ema = ta.ema(macd, length=9)
	# histogram = (macd - signal_ema)
	
	# is_downtrend = all(histogram[-i] < signal_ema[-i] for i in range(1, 6))
	
	# print(is_downtrend)
	# macd = MACD(stock_data['Close'])
	# signal_ema = macd.macd_signal()
	# histogram = macd.macd_diff()
	# is_downtrend = all(histogram[-i] < signal_ema[-i] for i in range(1, 6))
	# print(is_downtrend)
	# return is_downtrend
	# else:
		# return False

# Get the list of all stocks in India
# indian_stocks = yf.Tickers('AAPL').tickers
indian_stocks = ['KOTAKBANK.BO']
for item in indian_stocks:
	print(item)

# Find all the stocks in India with a previous downtrend and a hammer candlestick
hammer_stocks = [ticker for ticker in indian_stocks if has_previous_downtrend_and_hammer(ticker)]

# Print the list of all the stocks with a previous downtrend and a hammer candlestick
# print(hammer_stocks)

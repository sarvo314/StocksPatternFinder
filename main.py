import yfinance as yf
import mplfinance as mpf
import pandas_ta as ta
# from pyti.macd import macd
# import talib
# Define a function to check if a stock has a previous downtrend and a hammer candlestick
#percentage of the body

BODY_SIZE_PERCENTAGE_MIN = 19
BODY_SIZE_PERCENTAGE_MAX = 25
STOCK_DICT = {"SHOOTING_STAR": [],"HAMMER": []}
INDIAN_STOCKS = []
#the number of candles to check for hammer
CANDLES_TO_CHECK = 3
#period of data to check from
PERIOD_OF_DATA = '1mo'

'''
	ticker = symbol name
	BS = size of the candlestick
	LSS = Lower shadow size
	USS = upper shadow size,
'''
class Stock:
	def __init__(self, ticker, hammer, shootingStar):
		self.ticker = ticker
		self.hammer = hammer
		self.shootingStar = shootingStar
		self.CandleState = {}
	def GetStockName(self):
		return self.ticker
	def GetCandleStickStat(self):
		self.CandleState["Hammer"] = self.hammer
		self.CandleState["ShootingStar"] = self.shootingStar
		return self.CandleState

def check_patterns(ticker_symbol):
	stock_data = get_stock_data(ticker_symbol)
	if(not stock_data.empty):
		for i in range(-1*CANDLES_TO_CHECK, 0):
			if(candle_is_hammer(i, ticker_symbol)):
				print("We see a hammer:" + ticker_symbol)
			if(candle_is_shooting_star(stock_data, i, ticker_symbol)):
				print("We see a shooting star: " + ticker_symbol)
	
def get_candle_proportions(stock_data, candle_number):
	candle = stock_data.iloc[-1*candle_number]
	body_size = abs(last_candle['Open'] - last_candle['Close'])
	lower_shadow_size = abs(last_candle['Low'] - min(last_candle['Open'], last_candle['Close']))
	upper_shadow_size = abs(max(last_candle['Open'], last_candle['Close']) - last_candle['High'])
	total_size = body_size + lower_shadow_size + upper_shadow_size
	lower_shadow_size_percentage = (lower_shadow_size/total_size)*100
	upper_shadow_size_percentage = (upper_shadow_size/total_size)*100
	body_size_percentage = (body_size/total_size)*100
	
def candle_is_shooting_star(stock_data, candle_number, ticker_symbol):
#Check if the latest candlestick is a hammer
	# print(last_candle)
	
	
	
	is_hammer = lower_shadow_size > 1.8 * body_size
	
	
def candle_is_hammer(stock_data, candle_number, ticker_symbol):

	#Check if the latest candlestick is a hammer
	

	
	# print(last_candle)
	body_size = abs(last_candle['Open'] - last_candle['Close'])
	lower_shadow_size = abs(last_candle['Low'] - min(last_candle['Open'], last_candle['Close']))
	upper_shadow_size = abs(max(last_candle['Open'], last_candle['Close']) - last_candle['High'])
	total_size = body_size + lower_shadow_size + upper_shadow_size
	
	lower_shadow_size_percentage = (lower_shadow_size/total_size)*100
	upper_shadow_size_percentage = (upper_shadow_size/total_size)*100
	body_size_percentage = (body_size/total_size)*100
	is_hammer = lower_shadow_size > 1.8 * body_size
	
	return (is_hammer and body_size_percentage > BODY_SIZE_PERCENTAGE_MIN)

def get_stock_data(ticker_symbol):
	stock_data =  yf.download(ticker_symbol, period = PERIOD_OF_DATA)
	return stock_data

	
# def has_previous_downtrend_and_hammer(ticker_symbol):
	# Download historical data for the stock
	# if(stock_data): 
		# return False;
	# print(stock_data)
	
	
	# is_hammer = body_size < lower_shadow_size and body_size < upper_shadow_size and last_candle['Close'] > last_candle['Open']
	
			# print(f"Body size {body_size}, LowerBodySize {lower_shadow_size}, UpperBodySize {upper_shadow_size}")
	# Check if the stock has a previous downtrend
	# if is_hammer:
	# print(stock_data['Close'])
	# print(ta.macd(stock_data['Close']))
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

   
def read_data():
	myfile = open("output.txt")
	
	for line in myfile:
		for word in line.split():
			INDIAN_STOCKS.append(word)
	

# for item in indian_stocks:
# 	print(item)
# Find all the stocks in India with a previous downtrend and a hammer candlestick
read_data()
# print(f"TOTAL STOCKS TO BE SEARCHED {len(INDIAN_STOCKS)}")
# get_stock_data('MM.NS')
s = Stock("MM.NS", True, True)

# hammer_stocks = [ticker for ticker in INDIAN_STOCKS if has_previous_downtrend_and_hammer(ticker)]

# Print the list of all the stocks with a previous downtrend and a hammer candlestick
# print(hammer_stocks)

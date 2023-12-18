import pandas as pd
import yfinance as yf
import numpy
numpy.version.version
'1.22.0'
yf.version.version
'0.2.9'
from yahoofinancials import YahooFinancials
import time

# Set up Twilio credentials
#TWILIO_ACCOUNT_SID = 'your_account_sid'
#TWILIO_AUTH_TOKEN = 'your_auth_token'
#TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
#YOUR_PHONE_NUMBER = 'your_phone_number'

# Set up stock information
STOCK_SYMBOL = 'SPY'
ALERT_THRESHOLD = 350  # Set your desired alert threshold

# Initialize Twilio client
#twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def get_stock_price(STOCK_SYMBOL):
    stock = yf.Ticker(STOCK_SYMBOL)
    data = stock.history(period="1d")
    return data['Close'][0]

print(get_stock_price(STOCK_SYMBOL))

def get_stock_pricemean(STOCK_SYMBOL):
    stock = yf.Ticker(STOCK_SYMBOL)
    stock_data = stock.history(period="1d", start="2018-01-01")
    stock_values = stock_data["Close"]
    stock_dataarray = stock_values.values
    num_array = len(stock_dataarray)
    total = sum(stock_dataarray)
    mean = total/num_array
    return stock_data

print(get_stock_pricemean(STOCK_SYMBOL))


def get_stock_PE(STOCK_SYMBOL):
    stock = yf.Ticker(STOCK_SYMBOL)
    #stock_data = stock.info()
    return stock

SPY = yf.Ticker('PLTR')
print(get_stock_PE(STOCK_SYMBOL))
#print(SPY.get_info())
#print(SPY.get_a(nalysis()
#SPY.sustainability
#print(SPY.get_earnings())
#print(bruh)




import yfinance as yf
from sqlalchemy import create_engine
import pandas as pd

# Fetching historical data for apple stock
stock = yf.Ticker('AAPL')
data = stock.history(period='1y')
print(data.head())

# Storing data into MySql db
engine = create_engine('mysql+mysqlconnector://root:bbgun3001@localhost/stock_analysis')
data.to_sql('AAPL_data', engine, if_exists='replace', index=False)
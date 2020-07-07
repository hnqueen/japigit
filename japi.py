import sys
import pandas as pd
from alpha_vantage.timeseries import TimeSeries  # wrapper
#get the stock symbol
QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}"
API_KEY = '0ZW1LGOKLY20X8W8'

def getStockdata(symbol):
    try:
        print("Gathering info...")
        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])
    except:
        return "not found"

def main():
    outFile = open('japi.out','w')
    while 1:
        userInput = input("Enter Stock Symbol")
        if userInput != "Exit":
            serverData = 'The current price of {} is {}\n'.format(userInput, getStockdata(userInput))
            print(serverData)
            outFile.write(serverData)
        else:
            sys.exit("\nThank you for using the program!\n")
        main()


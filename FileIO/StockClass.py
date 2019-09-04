class StockClass:

    def __init__(self, ticker, date, opening, high, low, close, volume):
        self.ticker = ticker
        self.date = date
        self.open = opening
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def get_stock_details(self):
        return ("Ticker: " + self.ticker + "|Date: " + self.date + "|Open: " + self.open +
                "|Close: " + self.close + "|High: " + self.high + "|Low: " + self.low +
                "|Volume: " + self.volume)

    def get_ticker(self):
        return self.ticker

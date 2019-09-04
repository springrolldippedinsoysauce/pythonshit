from FileIO import StockClass
import pickle


class StockDriver:
    def __init__(self, file, save):
        self._count = 0
        self._i = 0
        self.stocks = []
        self.read_file(file)
        print(f'\nStock status: {self._count} processed\n')

    def get_data(self):
        return self.stocks

    def display(self):
        for e in self.stocks:
            line = e.split(',')
            if len(line) == 7:
                ticker = line[0]
                date = line[1]
                opening = line[2]
                high = line[3]
                low = line[4]
                close = line[5]
                volume = line[6]
                stock = StockClass.StockClass(ticker, date, opening, high, low, close, volume)
                print(stock.get_stock_details())

    def read_file(self, filename):
        try:
            file = open(filename, 'r')
            for line in file:
                self.stocks.append(line)
                self._count += 1
            file.close()
        except FileNotFoundError as e:
            print(e)

    def pickling(self, save):
        if save is not None and self.get_data() is not None:
            outfile = open(save, 'wb')
            pickle.dump(self.get_data(), outfile)
            outfile.close()
            print("Pickling complete!")


def unpickling(file):
    loaded = None
    if file is not None:
        infile = open(file, 'rb')
        loaded = pickle.load(infile)
        infile.close()
    return loaded

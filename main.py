import yfinance as yf
import utilities

if __name__ == '__main__':
    sector_list = list(["Energy", "Technology"])

    utilities.get_all_stocks_by_sector_list(sector_list)
import yfinance as yf
import utilities
import os

if __name__ == '__main__':
    os.environ["DEBUG"] = "True"

    sector_list = list(["Energy", "Technology"])

    energy_stocks = utilities.get_all_stocks_by_sector("Energy")
    p_stocks_list = list()
    ticker_list = list()

    for s in energy_stocks:
        ticker = yf.Ticker(s)
        try:
            if len(ticker_list) < 10:
                print(f"Informaçoes da  açao {s}:\n{ticker.info}")
                ticker_list.append(ticker)
            else:
                break
        except IndexError as e:
            print(f"Algum problema com a açao {s}")
            # print(e)
            p_stocks_list.append(s)

    print("Stocks problematicas:")
    print(p_stocks_list)

    for t in ticker_list:
        print(t.actions)

    t = yf.Ticker("AT")
    print(t.history(period="max"))


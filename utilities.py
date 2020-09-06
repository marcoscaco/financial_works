import os

def get_all_stocks_by_sector(sector):
    from get_all_tickers import get_tickers
    stocks = get_tickers.get_tickers_filtered(
        sectors=sector
    )

    stocks_list = list()

    if os.getenv("DEBUG"):
        print(f"LISTA DO SETOR: {sector}")

    for s in stocks:
        if os.getenv("DEBUG"):
            print(f"No setor {sector} temos a stock {s}")
        stocks_list.append(s)

    return stocks_list


"""
    :parameter sector_list A list() of sectors
    
    :returns A list() with list() of stocks
"""
def get_all_stocks_by_sector_list(sector_list):
    stocks_list = list()
    try:
        if len(sector_list) <= 0:
            print("A lista está vazia")
            return
        for sector in sector_list:
            stocks_list.append(
                get_all_stocks_by_sector(sector)
            )
        return stocks_list
    except TypeError as e:
        print("Lista inválida")
    except Exception:
        raise

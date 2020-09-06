def get_all_stocks_by_sector(sector):
    from get_all_tickers import get_tickers
    stocks = get_tickers.get_tickers_filtered(
        sectors=sector
    )

    print(f"LISTA DO SETOR: {sector}")

    for s in stocks:
        print(f"No setor {sector} temos a stock {s}")


def get_all_stocks_by_sector_list(sector_list):
    for sector in sector_list:
        get_all_stocks_by_sector(sector)

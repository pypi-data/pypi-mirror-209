import pandas as pd

def get_stock_symbols(*filepaths):
    symbols = []
    for filepath in filepaths:
        df = pd.read_csv(filepath)
        symbols.extend(df['symbol'].tolist())
    return symbols

symbols = get_stock_symbols('D:\training\Ticker\NASDAQ.csv', 'D:\training\Ticker\NYSE.csv')
print(symbols)

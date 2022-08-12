import FinanceDataReader as fdr
nas_df = fdr.StockListing('NASDAQ')
print(nas_df.head(10))
AAPL = fdr.DataReader('AAPL')
print(AAPL.head())
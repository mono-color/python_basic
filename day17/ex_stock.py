import FinanceDataReader as fdr
import pandas as pd


# 삼성 005930
def fn_get_stock(p_code, p_start, p_end):
    df = fdr.DataReader(p_code, p_start, p_end)
    print(df.head())
    # 인덱스에 있던 데이터를 -> 컬럼으로
    # 인덱스 자리를 0 ~
    df = df.reset_index()
    print(df.head())
    seq = df['Date'].dt.strftime('%Y-%m-%d')
    # 스트링으로 d
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Change']].astype(str)
    df['Date'] = seq
    file_nm = '{0}_{1}_{2}.xlsx'.format(p_code, p_start.replace('-', ''), p_end.replace('-', ''))
    writher = pd.ExcelWriter(file_nm, engine='openpyxl')
    df.to_excel(writher, 'Sheet1')
    writher.save()

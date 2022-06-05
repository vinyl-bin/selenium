from unicodedata import category
import pandas as pd

df = pd.read_excel('naver2.xlsx', usecols=[3,4], header=None, index_col=None)
print(df)

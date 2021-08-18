import pandas as pd

path= '/home/gustavo/Documentos/desenvolvimento/web/cidadania_ja/politicians.csv'

data = pd.read_csv(path, encoding='utf-8')

print(data.head())

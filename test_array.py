import pandas as pd

data = pd.read_csv('products_final.csv')
for row in data.iterrows():
    print(row)
    break
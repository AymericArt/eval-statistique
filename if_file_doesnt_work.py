#Exo 1
#Les KPI sont des indicateurs clés de performance

#Exo 2
import pandas as pd
import numpy as np

#Exo 3
df = pd.read_csv('./data/eval_data.csv')

#Exo 4
df.head(12)

#Exo 5
df.shape

#Exo 6
df.info()

#Exo 7
df.describe()

#Exo 8
df.item_name.mode()

#Exo 9
df['quantity'].sum()

#Exo 10
df['item_price'] = df['item_price'].fillna(0.0).replace('\$|,', '', regex=True)
df['item_price'] = pd.to_numeric(df['item_price'])
resultCA = (df['quantity'] * df['item_price']).sum()
resultCA

#Exo 11
resultMean = (df['quantity'] * df['item_price']).mean()
resultMean
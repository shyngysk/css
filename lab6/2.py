import pandas as pd
import numpy as np
import seaborn as sns
#1
# df = pd.read_excel("catalog_products.xlsx")
# print(df.shape)
# print(df.head(5))
# print(df.isnull().sum())
# print(df.dtypes)

#2
# df = pd.read_excel("catalog_products.xlsx")
# for col in df.columns:
#     df[col] = pd.to_numeric(df[col], errors='coerce')
# numeric_cols = df.select_dtypes(include=['number']).columns
# df[numeric_cols] = df[numeric_cols].astype(float)
# df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
# print(df[numeric_cols].isnull().sum())
# print(df[numeric_cols].dtypes)

#3
# df = pd.read_excel("catalog_products.xlsx")
# df["total_value"] = df["col_2"] * df["col_3"]
# df["double_stock"] = df["col_4"] * 2
# df["log_price"] = np.log(df["col_2"])
# print(df[["total_value", "double_stock", "log_price"]].head())

#4
# df = pd.read_excel("catalog_products.xlsx")
# a = df[(df["col_2"] > 500) & (df["col_7"] == "Electronics")]
# print(a.head())

#5
# df = pd.read_excel("catalog_products.xlsx")
# a = df.groupby("col_7").agg(
#     mean_price=("col_2", "mean"),
#     max_price=("col_2", "max"),
#     total_quantity=("col_3", "sum")
# )
# b = df.rename(columns={"category": "col_7"})
# print(b)

#6
# df = pd.read_excel("catalog_products.xlsx")
# a = ["col_2", "col_3", "col_4", "col_5", "col_6", "col_7", "col_8", "col_9", "col_10", "col_11"]
# b = df[a].select_dtypes(include=['number'])
# stats = pd.DataFrame([
#     {'column': b.columns, 'mean': b.mean().values, 'median': b.median().values, 'std': b.std().values}
# ])
# print(stats)

#7
# df = pd.read_excel("catalog_products.xlsx")
# mean = df['col_2'].mean()
# std = df['col_2'].std()
# lim = mean + 3 * std
# anomalies = df[df['col_2'] > lim]
# print(anomalies.head())
# print(lim)

#8
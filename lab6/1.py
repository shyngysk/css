#1
import pandas as pd
import numpy as np
from numpy.ma.core import anomalies, correlate

df = pd.read_excel("catalog_products.xlsx")
# print("DataFrame form:", df.shape)
# print("\nData types:")
# print(df.dtypes)
# print("\nMissed values by columns:")
# print(df.isnull().sum())
# print("\nFirst 5 strings:")
# print(df.head(5))

#2
# numeric_cols = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6']
# for col in df.columns:
#     df[col] = pd.to_numeric(df[col], errors='coerce')
# df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
# print("Типы данных после преобразования:")
# print(df[numeric_cols].dtypes.head())
# print("\nКоличество пропусков в числовых колонках:")
# print(df[numeric_cols].isnull().sum())
# print("\nПервые 5 строк числовых колонок:")
# print(df[numeric_cols].head())

#3
# df['total_value'] = df['col_2'] * df['col_3']
# df['double_stock'] = df['col_4'] * 2
# df['log_price'] = np.log(df['col_2'])
# print("Новые показатели:")
# print(df[['total_value', 'double_stock', 'log_price']].head())

#4
# electronics_expensive = df[(df['col_2'] > 500) & (df['col_7'] == 'Electronics')]
# print("Количество найденных товаров:", len(electronics_expensive))
# print("\nПервые 5 строк дорогих товаров электроники:")
# print(electronics_expensive.head())

#5
# category = df.groupby('col_7').agg(
#     mean_price=('col_2', 'mean'),
#     max_price=('col_2', 'max'),
#     total=('col_3', 'sum')
# )
# category = category.rename(columns={'col_7': 'category'})
# print("Анализ по категориям:")
# print(category)

#6
# a = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8', 'col_9', 'col_10', 'col_11']
# s = df[a].select_dtypes(include=['number'])
# stats = pd.DataFrame([
#     {'column': s.columns,
#     'mean': s.mean().values,
#     'median': s.median().values,
#     'std': s.std().values}
# ])
# print("Суммарная статистика по колонкам:")
# print(s)

#7
# mean = df['col_2'].mean()
# std = df['col_2'].std()
# upperlimit = mean + 3 * std
# anomalies = df[df['col_2'] > upperlimit]
# print(f"Средняя цена: {mean:.2f}")
# print(f"Стандартное отклонение: {std:.2f}")
# print(f"Порог аномалий: {upperlimit:.2f}")
# print(f"\nНайдено аномальных товаров: {len(anomalies)}")
# print("\nПервые 5 строк с аномалиями:")
# print(anomalies.head())

#8
# numeric_df = df[a].select_dtypes(include=['number'])
# correlation_matrix = numeric_df.corr()
# print("Корреляционная матрица:")
# print(correlation_matrix)

#9
import matplotlib.pyplot as plt
# plt.figure(figsize=(10,6))
# plt.hist(df['col_2'], bins=50, color='blue', edgecolor='black')
# plt.title('Распределение цен товаров (col_2)', fontsize=15)
# plt.xlabel('Цена товаров', fontsize=12)
# plt.ylabel('Количество товаров', fontsize=12)
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.show()

#10
import seaborn as sns
# sns.set_theme(style="darkgrid")
# plt.figure(figsize=(10,6))
# sns.regplot(data=df, x='col_2', y='col_3', scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
# plt.title('Взаимосвязь цены и количества на складе', fontsize=14)
# plt.xlabel('Цена (col_2)', fontsize=12)
# plt.ylabel('Количество на складе (col_3)', fontsize=12)
# plt.show()

#11
# plt.figure(figsize=(12, 7))
# sns.barplot(data=df, x='col_7', y='col_2', palette='viridis')
# plt.title('Средняя цена по категориям')
# plt.xticks(rotation=45)
# plt.show()

#12
# sel = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']
# df_subset = df[sel]
# sns.pairplot(df_subset, hue='col_7', palette='viridis', corner=True)
# plt.suptitle('Парные диаграммы характеристик товаров', y=1.02, fontsize=14)
# plt.show()

#13
# selected = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8', 'col_9', 'col_10', 'col_11']
# b = df[selected].select_dtypes(include=['number']).corr()
# plt.figure(figsize=(12,10))
# sns.heatmap(b, annot=True, cmap='coolwarm', fmt='.2f', linewidth=0.5)
# plt.title('Тепловая карта корреляции характеристик товаров', fontsize=16)
# plt.show()

#14
# cols = ['col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8', 'col_9', 'col_10', 'col_11', 'total_value', 'double_stock', 'log_price']
# final = df[cols]
# final.to_excel('catalog_analysis.xlsx', index=False)
# print("Файл 'catalog_analysis.xlsx' успешно сохранен!")

#15
# summary = df.groupby('col_7').agg(
#     count=('col_1', 'count'),
#     mean_price=('col_2', 'mean'),
#     total=('col_3', 'sum'),
#     mean_log_price=('log_price', 'mean')
# )
# summary = summary.rename(columns={'col_7': 'category'})
# summary = summary.round(2)
# print("Финальный агрегированный отчет по категориям:")
# print(summary.head())

#16
# idx = df.groupby("col_7")["col_2"].idxmax()
# res = df.loc[idx]
# res = res[["col_1", "col_2", "col_7"]]
# res = res.sort_values("col_7")
# print(res)

#17
# df['total_values'] = df['col_1'] * df['col_3']
# sorted = df.sort_values("total_values", ascending=False).head(10)
# print(sorted[["col_1", "col_2", "col_3", "total_values"]])

#18
# a = [0, 50, 200, 500, 1000, float("inf")]
# b = ["0-50", "50-200", "200-500", "500-1000", ">1000"]
# df["price_range"] = pd.cut(df["col_2"], bins=a, labels=b, include_lowest=True)
# count = df["price_range"].value_counts().sort_index()
# res = count
# res.columns = ["price_range", "count"]
# print(res)

#19
# df["total"] = df["col_1"] * df["col_3"]
# ctg = df.groupby("col_7")["total"].sum().sort_values(ascending=False)
# top = ctg.idxmax()
# print(top)
# print(ctg.head())
# res = ctg.reset_index()
# res.columns = ["category", "total_value"]
import seaborn as sns
import matplotlib.pyplot as plt
# plt.figure(figsize = (10,10))
# sns.barplot(data=res, x="category", y="total_value")
# plt.title("Sum")
# plt.xticks(rotation = 45)
# plt.show()

#20
# a = df.groupby("col_7").agg(
#     mean_price=("col_2", "mean"),
#     mean_quantity=("col_3", "mean")
# )
# plt.figure(figsize = (10,6))
# sns.scatterplot(
#     data=a,
#     x="mean_price",
#     y="mean_quantity",
#     hue="col_7",
#     s=100
# )
# plt.title("Средняя цена vs средний запас по категориям")
# plt.xlabel("Средняя цена")
# plt.ylabel("Средний запас")
# plt.legend(title="Категория")
# plt.show()

#21
# a = df.groupby("col_7")["col_2"].std().reset_index()
# a.columns = ["category", "std_price"]
# plt.figure(figsize=(10,5))
# sns.barplot(data=a, y="category", x="std_price")
# plt.title("Разброс цен по категориям")
# plt.xlabel("Стандартное отклонение цены")
# plt.ylabel("Категория")
# plt.show()

#22
# ns = df[df["col_3"] == 0][["col_1", "col_7", "col_2"]].head(10)
# print(ns)

#23
# a = df.groupby("col_7")["col_1"].count().sort_values(ascending=False).head(5)
# a = a.reset_index()
# a.columns = ["category", "count"]
# plt.figure(figsize = (10,10))
# sns.barplot(data=a, x="category", y="count")
# plt.title("Топ-5 категорий по количеству товаров")
# plt.xlabel("Категория")
# plt.ylabel("Количество товаров")
# plt.xticks(rotation=45)
# plt.show()

#24
# a = df.sort_values("col_3", ascending=False).head(10)
# plt.figure(figsize = (10,10))
# sns.barplot(data=a, x="col_3", y="col_1")
# plt.title("Top 10 items")
# plt.xlabel("Amount")
# plt.ylabel("Item")
# plt.show()

#25
# a = [0, 50, 200, 500, 1000, float("inf")]
# b = ["0-50", "50-200", "200-500", "500-1000", ">1000"]
# df["price_range"] = pd.cut(df["col_2"], bins=a, labels=b, include_lowest=True)
# pivot = df.pivot_table(index="col_7", columns="price_range", values="col_1", aggfunc="count", fill_value=0)
# plt.figure(figsize = (10,10))
# sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu")
# plt.title("Распределение товаров по категориям и ценам")
# plt.xlabel("Диапазон цены")
# plt.ylabel("Категория")
# plt.show()

#26
# a = df.groupby("col_7").agg(
#     mean_price=("col_2", "mean"),
#     mean_quantity=("col_3", "mean")
# ).reset_index()
# plt.figure(figsize = (10,10))
# sns.scatterplot(data=a, x="mean_price", y="mean_quantity", hue="col_7", s=100)
# plt.title("Категории: средняя цена vs средний запас")
# plt.xlabel("Средняя цена")
# plt.ylabel("Средний запас")
# plt.legend(title="Категория")
# plt.show()

#27
# a = df.groupby("col_7")["col_2"].std().reset_index()
# a.columns = ["category", "std"]
# plt.figure(figsize = (8,8))
# sns.barplot(x="category", y="std", data=a)
# plt.title("Standard Deviation by categories")
# plt.xlabel("Category")
# plt.ylabel("Standard Deviation")
# plt.show()

#28
# a = df[df["col_3"] == 0][["col_1", "col_7", "col_2"]].head(10)
# print(a)

#29
# a = df.groupby("col_7")["col_1"].count().sort_values(ascending=False).head(5)
# a = a.reset_index()
# a.columns = ["category", "count"]
# plt.figure(figsize = (10,10))
# sns.barplot(data=a, x="category", y="count")
# plt.show()

#30
# a = df.sort_values("col_3", ascending=False).head(10)
# plt.figure(figsize = (10,10))
# sns.barplot(data=a,x="col_3", y="col_1")
# plt.title("Топ-10 товаров по запасу")
# plt.xlabel("Количество на складе")
# plt.ylabel("Товар")
# plt.show()

#31
# a = [0,50,200,500,1000,float("inf")]
# b=["0-50","50-200","200-500","500-1000",">1000"]
# df["price_range"] = pd.cut(df["col_2"], bins=a, labels=b, include_lowest=True)
# pivot = df.pivot_table(index="col_7", columns="price_range", values="col_1", aggfunc="count", fill_value=0)
# plt.figure(figsize = (10,10))
# sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu")
# plt.show()

#32
# plt.figure(figsize=(10,6))
# sns.regplot(data=df,x="col_2",y="col_5",scatter_kws={"alpha": 0.5},line_kws={"color": "red"})
# plt.title("Зависимость цены и рейтинга товаров")
# plt.xlabel("Цена")
# plt.ylabel("Рейтинг")
# plt.show()

#33
# z = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6']
# df_subset = df[z]
# sns.pairplot(df_subset)
# plt.suptitle("Парные зависимости характеристик товаров", y=1.02)
# plt.show()

#34
# mean = df["col_2"].mean()
# std = df["col_2"].std()
# s_mean = df["col_3"].mean()
# s_std = df["col_3"].std()
# pricelim = mean + 3 * std
# slim = s_mean + 3 * s_std
# extreme_items = df[
#     (df["col_2"] > pricelim) | (df["col_3"] > slim)
# ]
# print(extreme_items)

#35
# df["total_value"] = df["col_2"] * df["col_3"]
# df["double_stock"] = df["col_4"] * 2
# df["log_price"] = np.log(df["col_2"])
# summary = df.groupby("col_7").agg(
#     mean_price=("col_2", "mean"),
#     mean_stock=("col_3", "mean"),
#     total_stock=("col_3", "sum")
# ).reset_index()
# a = df.sort_values("col_3", ascending=False).head(10)
# b = df.sort_values("total_value", ascending=False).head(10)
# with pd.ExcelWriter("catalog_final_report.xlsx") as f:
#     df.to_excel(f, sheet_name="data", index=False)
#     summary.to_excel(f, sheet_name="summary", index=False)
#     a.to_excel(f, sheet_name="top_stock", index=False)
#     b.to_excel(f, sheet_name="top_value", index=False)
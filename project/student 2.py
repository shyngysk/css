import pandas as pd
import numpy as np
from numpy.ma.core import equal
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bank_advanced_dataset.csv")
#1
numeric_data = ['Age', 'Income', 'Balance', 'Credit_Score', 'Loan_Amount', 'Transactions_Last_Month', 'Cards_Count', 'Branch_Visits_Last_Year', 'Complaints_Last_Year']
# print(df[numeric_data].head(5))

#2
cols = ['Age', 'Income', 'Balance', 'Credit_Score', 'Loan_Amount']
a = pd.DataFrame({
    "Mean": df[cols].mean(),
    "Median": df[cols].median(),
    "Std": df[cols].std()
})
# print(a)

#3
c = df['Income'].values
d = df['Balance'].values
e = np.where((c > 80000) & (d > 50000))[0]
f = df.loc[e, ['Customer_ID', 'Income', 'Balance']].head(10)
# print(f)

#4
dict = df['Account_Type'].value_counts().head(2).to_dict()
# print(dict)

#5
region = set(df['Region'])
loanstatus = set(df['Loan_Status'])
# print("Regions:", len(region),"\n" "Loan Statuses:", len(loanstatus))

#6
high_income = (
    row for _, row in df.iterrows() if row['Income'] >= 100000
)
df['loan_ratio'] = df.apply(
    lambda x: x['Loan_Amount'] / (x['Balance'] + 1),
    axis = 1
)
# for i, client in enumerate(high_income):
#     if i >= 10:
#         break
#     print(client['Customer_ID'], client['Income'], client['loan_ratio'])

#7
pivot = pd.pivot_table(df, index='Region', columns='Account_Type', values='Balance', aggfunc='mean')
max_value = pivot.max().max()
res = pivot.stack().idxmax()
# print("Max mean:", max_value, '\n'"Region:", res)

#8
df.to_csv("student2_loan_ratio.csv", index=False)
pivot.to_excel("student2_region_account.xlsx")
ndf = pd.read_csv("student2_loan_ratio.csv")
# print(np.allclose(
#     df.select_dtypes(include=['number']), ndf.select_dtypes(include=['number'])
# ))

#9
# plt.figure(figsize = (10,10))
# plt.hist(df["Age"], bins=15)
# plt.xlabel("Age")
# plt.ylabel("Amount")
# plt.title("Age Histogram")
# plt.grid(True)
# plt.savefig("student2_age_histogram.png")
# plt.show()

# plt.figure(figsize = (10,10))
# plt.scatter(df['Income'], df['Balance'])
# plt.xlabel("Income")
# plt.ylabel("Balance")
# plt.title("Income vs Balance")
# plt.grid(True)
# plt.savefig("student2_income_balance.png")
# plt.show()

#10
# plt.figure(figsize=(8,8))
# sns.countplot(x="Account_Type", data=df)
# plt.xlabel("Account Type")
# plt.ylabel("Count")
# plt.title("Account Type counts")
# plt.savefig("student2_acctype_countplot.png")
# plt.show()
#
# plt.figure(figsize=(8,8))
# sns.boxplot(x='loan_ratio', y='Region', data=df)
# plt.xlabel("Loan Ratio")
# plt.ylabel("Region")
# plt.title("Loan Ratio Boxplot")
# plt.savefig("student2_loan_ratio.png")
# plt.show()
#
# plt.figure(figsize=(8,8))
# corr = df.corr(numeric_only=True)
# sns.heatmap(corr)
# plt.title("Correlation Heatmap")
# plt.savefig("student2_correlation_heatmap.png")
# plt.show()
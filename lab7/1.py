import numpy as np
import pandas as pd
df = pd.read_excel("catalog_products.xlsx")

#1
# print(df.head(5))
# print(df.shape)
# print(df.dtypes)
# print(df.isnull().sum())

#2
# num = df.select_dtypes(include=['int', 'float']).columns
# df[num] = df[num].astype(float)
# for i in num:
#     mean = df[i].mean()
#     df[i] = df[i].fillna(mean)
# a = df.select_dtypes(include=['object']).columns
# df = df.dropna(subset=a)
# print(df.dtypes)
# print(df.isnull().sum())
# print(df.shape)

#3
import numpy as np
df['total_value'] = df['col_2'] * df['col_3']
df['log_price'] = np.log(df['col_2'])
df['double_stock'] = df['col_4'] * 2
# print(df[['total_value', 'log_price', 'double_stock']])

#4
import matplotlib.pyplot as plt
# plt.figure(figsize = (10,10))
# plt.hist(df['col_2'])
# plt.title('Histogram of column 2')
# plt.show()
# plt.figure(figsize = (10,10))
# plt.scatter(df['col_2'], df['col_3'])
# plt.title('Scatter plot of column 2')
# plt.xlabel('col_2')
# plt.ylabel('col_3')
# plt.show()
# plt.figure(figsize = (10,10))
# df.boxplot(column='col_2', by='col_7')
# plt.title('Boxplot of column 2')
# plt.xlabel('col_7')
# plt.ylabel('col_2')
# plt.show()

#5
mean = df['col_2'].mean()
std = df['col_2'].std()
low = mean - 3 * std
high = mean + 3 * std
df_clean = df[
    (df['col_2'] >= low) &
    (df['col_2'] <= high)
]
# print(df_clean.shape)

#6
df_encoded = pd.get_dummies(df, columns=['col_7'])
# print(df_encoded.dtypes)
text_columns = df_encoded.select_dtypes(include=['object']).columns
# print(text_columns)
# if len(text_columns) == 0:
    # print("\nВсе признаки теперь числовые.")
# else:
#     print("\nОстались текстовые признаки.")

#7
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    accuracy_score,
    confusion_matrix
)
import seaborn as sns
df_encoded = df_encoded.select_dtypes(exclude=['object'])
y = df_encoded['col_2']
X = df_encoded.drop(columns=['col_2'])
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# print("Train shape:", X_train.shape)
# print("Test shape:", X_test.shape)

#8
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
mae_lr = mean_absolute_error(y_test, y_pred)
mse_lr = mean_squared_error(y_test, y_pred)
# print("MAE:", mae_lr)
# print("MSE:", mse_lr)

#9
important_features = [col for col in X.columns]
X2 = df_encoded[important_features]
X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2,
    y,
    test_size=0.2,
    random_state=42
)
lr2 = LinearRegression()
lr2.fit(X2_train, y2_train)
y2_pred = lr2.predict(X2_test)
mae_lr2 = mean_absolute_error(y2_test, y2_pred)
mse_lr2 = mean_squared_error(y2_test, y2_pred)
# print("MAE:", mae_lr2)
# print("MSE:", mse_lr2)

#10
plt.figure(figsize=(7, 6))
plt.scatter(y_test, y_pred)
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val])
plt.xlabel("Истинная цена")
plt.ylabel("Предсказанная цена")
plt.title("Истинная vs Предсказанная цена")
# plt.show()
errors = abs(y_test - y_pred)
worst_predictions = pd.DataFrame({
    'real_price': y_test,
    'predicted_price': y_pred,
    'error': errors
})
# print(worst_predictions.sort_values(by='error', ascending=False).head())

#11
scaler = StandardScaler()
scale_cols = [
    'col_3',
    'col_4',
    'total_value',
    'double_stock',
    'log_price'
]
existing_scale_cols = [c for c in scale_cols if c in df_encoded.columns]
df_encoded[existing_scale_cols] = scaler.fit_transform(
    df_encoded[existing_scale_cols]
)
print(df_encoded[existing_scale_cols].mean())

#12
tree = DecisionTreeRegressor(random_state=42)
tree.fit(X_train, y_train)
importance = pd.DataFrame({
    'feature': X.columns,
    'importance': tree.feature_importances_
})
importance = importance.sort_values(
    by='importance',
    ascending=False
)
print(importance.head(10))
plt.figure(figsize=(10, 6))
plt.bar(
    importance['feature'][:10],
    importance['importance'][:10]
)
plt.xticks(rotation=90)
plt.title("Feature Importance")
# plt.show()

#13
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
X_poly_train, X_poly_test, y_poly_train, y_poly_test = train_test_split(
    X_poly,
    y,
    test_size=0.2,
    random_state=42
)
poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_poly_train)
y_poly_pred = poly_model.predict(X_poly_test)
mae_poly = mean_absolute_error(y_poly_test, y_poly_pred)
mse_poly = mean_squared_error(y_poly_test, y_poly_pred)
# print("MAE:", mae_poly)
# print("MSE:", mse_poly)

#14
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)
y_knn_pred = knn.predict(X_test)
mae_knn = mean_absolute_error(y_test, y_knn_pred)
mse_knn = mean_squared_error(y_test, y_knn_pred)
# print("MAE:", mae_knn)
# print("MSE:", mse_knn)

#15
for category in df['col_7'].unique():
    temp = df[df['col_7'] == category]
    if len(temp) < 10:
        continue
    temp_encoded = pd.get_dummies(temp)
    temp_encoded = temp_encoded.select_dtypes(exclude=['object'])
    y_cat = temp_encoded['col_2']
    X_cat = temp_encoded.drop(columns=['col_2'])
    X_train_cat, X_test_cat, y_train_cat, y_test_cat = train_test_split(
        X_cat,
        y_cat,
        test_size=0.2,
        random_state=42
    )
    model_cat = LinearRegression()
    model_cat.fit(X_train_cat, y_train_cat)
    pred_cat = model_cat.predict(X_test_cat)
    mae_cat = mean_absolute_error(y_test_cat, pred_cat)
    # print(category, "MAE =", mae_cat)

#16
for category in df['col_7'].unique():
    temp = df[df['col_7'] == category]
    if len(temp) < 10:
        continue
    temp_encoded = pd.get_dummies(temp)
    temp_encoded = temp_encoded.select_dtypes(exclude=['object'])
    y_cat = temp_encoded['col_2']
    X_cat = temp_encoded.drop(columns=['col_2'])
    X_train_cat, X_test_cat, y_train_cat, y_test_cat = train_test_split(
        X_cat,
        y_cat,
        test_size=0.2,
        random_state=42
    )
    model_cat = LinearRegression()
    model_cat.fit(X_train_cat, y_train_cat)
    pred_cat = model_cat.predict(X_test_cat)
    plt.figure(figsize=(6, 5))
    plt.scatter(y_test_cat, pred_cat)
    min_val = min(y_test_cat.min(), pred_cat.min())
    max_val = max(y_test_cat.max(), pred_cat.max())
    plt.plot([min_val, max_val], [min_val, max_val])
    plt.title(f'Категория: {category}')
    plt.xlabel("Истинная цена")
    plt.ylabel("Предсказанная цена")
    # plt.show()

#17
cv_mae = -cross_val_score(
    lr,
    X,
    y,
    cv=5,
    scoring='neg_mean_absolute_error'
)
cv_mse = -cross_val_score(
    lr,
    X,
    y,
    cv=5,
    scoring='neg_mean_squared_error'
)
# print("Средний MAE:", cv_mae.mean())
# print("Средний MSE:", cv_mse.mean())

#18
def price_category(price):
    if price < 100:
        return 0
    elif price <= 500:
        return 1
    else:
        return 2
df_encoded['price_class'] = df_encoded['col_2'].apply(price_category)
X_cls = df_encoded.drop(columns=['price_class', 'col_2'])
y_cls = df_encoded['price_class']
X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
    X_cls,
    y_cls,
    test_size=0.2,
    random_state=42
)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train_cls, y_train_cls)
y_cls_pred = clf.predict(X_test_cls)
acc = accuracy_score(y_test_cls, y_cls_pred)
# print("Accuracy:", acc)

#19
cm = confusion_matrix(y_test_cls, y_cls_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
# plt.show()

#20
df_encoded['predicted_price'] = lr.predict(X)
df_encoded['predicted_class'] = clf.predict(X_cls)
df_encoded.to_excel(
    'catalog_ml_predictions.xlsx',
    index=False
)
# print("DONE")


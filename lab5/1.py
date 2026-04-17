#1
from itertools import product


class User:
    def __init__(self, id, name, email):
        self._id = id
        self._name = name.strip().title()
        self._email = email.strip().lower()
        if "@" not in self._email:
            raise ValueError("Invalid email")
    def __del__(self):
        print(f"User {self._name} deleted")
    def __str__(self):
        return f"User(id='{self._id}', name='{self._name}', email='{self._email}')"
# u = User(1, " john doe ", "John@Example.COM")
# print(u)

#2
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")
        if len(parts) != 3:
            raise ValueError("Invalid format")
        user_id = int(parts[0].strip())
        name = parts[1].strip()
        email = parts[2].strip()
        return cls(user_id, name, email)
u = User.from_string("2, Alice Wonderland , alice@wonder.com")
print(u)

#3
class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name.strip().title()
        self.price = price
        self.category = category
    def __eq__(self, other):
        return isinstance(other, Product) and self.id == other.id and self.name == other.name and self.category == other.category
    def __hash__(self):
        return hash((self.id, self.name, self.category))
    def to_dict(self):
        return {"id": self.id, "name": self.name, "category": self.category}
    def __str__(self):
        return f"Product(id='{self.id}', name='{self.name}', price={self.price}, category={self.category})"

#4
class Inventory:
    def __init__(self):
        self._items = []
    def add_product(self, product: Product):
        if product.id not in [i.id for i in self._items]:
            self._items.append(product)
    def remove_product(self, product_id: int):
        self._items = [i for i in self._items if i.id != product_id]
    def get_product(self, product_id: int):
        for i in self._items:
            if i.id == product_id:
                return i
        return None
    def get_all_products(self):
        return list(self._items)
    def unique_products(self):
        return set(self._items)
    def to_dict(self):
        return {i.id: i for i in self._items}

#5
    def filter_by_price(self, min_price: float):
        return [i for i in self._items if (lambda x: x >= min_price)(i.price)]
# inv = Inventory()
# inv.add_product(Product(1, "Laptop", 1200.0, "Electronics"))
# inv.add_product(Product(2, "Mouse", 25.0, "Electronics"))
# expensive = inv.filter_by_price(100.0)
# print([p.name for p in expensive])

#6
from datetime import datetime
class Logger:
    @staticmethod
    def log_action(self, user: User, action: str, product: Product, filename: str):
        with open(filename, "a") as f:
            f.write(f"{timestamp};{user_id};{action};{product_id}\n")
    @staticmethod
    def read_logs(self, filename: str):
        with open(filename, "r") as f:
            lines = f.readlines()
            res = []
            for line in lines:
                parts = line.strip().split(";")
                log = {
                    "timestamp": int(parts[0]),
                    "user_id": int(parts[1]),
                    "action": parts[2],
                    "product_id": int(parts[3]),
                }
                res.append(log)

#7
class Order:
    def __init__(self, id, user, products):
        self.id = id
        self.user = user
        self.products = products
    def add_product(self, product: Product):
        if product.id not in [i.id for i in self.products]:
            self.products.append(product)
    def remove_product(self, product_id: int):
        self.products = [i for i in self.products if i.id != product_id]
    def total_price(self):
        return sum(i.price for i in self.products)
    def __str__(self):
        return (f"Order(id={self.id}, user_id={self.user.id}, products={[i.name for i in self.products]})")

#8
    def most_expensive_products(self, n: int):
        return sorted(self.products, key=lambda x: x.price, reverse=True)[:n]

#9
def stream_products(products):
    for product in products:
        yield product.price

#10
class OrderIterator:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.orders):
            raise StopIteration
        order = self.orders[self.index]
        self.index += 1
        return order

#11
import numpy as np
products = [
    Product(1,"Laptop",1200.0,"Electronics"),
    Product(2,"Mouse",25.0,"Electronics")
]
a = np.array([i.price for i in products])
# print(a)

#12
b = np.median(a)
c = np.average(a)
# print(b, c)

#13
def normalize_prices(n):
    return (n - n.min()) / (n.max() - n.min())
d = normalize_prices(a)
# print(d)

#14
productss = [Product(1,"Laptop",1200.0,"Electronics"), Product(2,"T-Shirt",20.0,"Clothing")]
ctg = np.array([i.category for i in productss])
# print(ctg)

#15
def unique(arr):
    return len(set(arr))
arr = np.array([i.category for i in productss])
# print(unique(arr))

#16
prods = [
    Product(1,"Laptop",1200.0,"Electronics"),
    Product(2,"Mouse",25.0,"Electronics"),
    Product(3,"Monitor",450.0,"Electronics")
]
m = np.array([i.price for i in prods])
n = np.average(m)
b = np.array([i for i in prods if i.price > n])
# for i in b:
#     print(i)

#17
o = np.array([i.price * 0.9 for i in prods])
# print(o)

#18
u1 = User(1, "John", "john@gmail.com")
u2 = User(2, "Karen", "karen@gmail.com")
orders = [
    Order(1,u1,[Product(1,"Laptop",1200.0,"Electronics")]),
    Order(2,u2,[Product(2,"Mouse",25.0,"Electronics"), Product(1,"Laptop",1200.0,"Electronics")])]
arr = np.array([[order.total_price() for order in orders]])
# print(arr)

#19
brr = np.average(arr)
# print(brr)

#20
f = np.array([1200.0, 900.0, 1500.0])
l = np.where(f>1000)[0]
# print(l)

#21
from datetime import datetime
import pandas as pd
users = [
    User(1, "Jaden", "jaden@gmail.com"),
    User(2, "Alice", "alice@gmail.com")
]
df = pd.DataFrame([
    {
        "id": u._id,
        "name": u._name,
        "email": u._email,
        "registration_date": datetime.now().date()
    }
    for u in users
])
# print(df)

#22
products = [Product(1,"Laptop",1200.0,"Electronics"), Product(2,"T-Shirt",20.0,"Clothing")]
pf = pd.DataFrame([
    {
        "id": p.id,
        "name": p.name,
        "category": p.category,
        "price": p.price
    }
    for p in products
])
# print(df)

#23
df_users = pd.DataFrame([
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alice"}
])
df_orders = pd.DataFrame([
    {"order_id": 101, "user_id": 1, "total": 1200},
    {"order_id": 103, "user_id": 1, "total": 500},
    {"order_id": 102, "user_id": 2, "total": 900},
])
df = pd.merge(df_users, df_orders, left_on = "id", right_on = "user_id")
df = df.rename(columns={"name": "user_name"})
df = df[["order_id", "user_name", "total"]]
# print(df)

#24
filtered = df[df["total"] > 1000]
# print(filtered)

#25
res = df.groupby("user_name")["total"].sum()
res.column = ["user_name", "total_sum"]
# print(res)

#26
result = df.groupby("user_name")["total"].mean()
result.column = ["user_name", "total_mean"]
# print(result)

#27
res2 = df.groupby("user_name")["order_id"].count()
res2.column = ["user_name", "total_count"]
# print(res2)

#28
prod_order = pd.DataFrame([
    {"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 25, "category": "Electronics"},
    {"id": 3, "name": "Shirt", "price": 20, "category": "Clothing"},
])
res3 = prod_order.groupby("category")["price"].mean()
res3.column = ["prod_name", "total_mean"]
# print(res3)

#29
qr = pd.DataFrame([
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 25}
])
qr["discounted_price"] = qr["price"] * 0.9
# print(qr)

#30
bd = pd.DataFrame([
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Monitor", "price": 450}
])
bd = bd.sort_values("price", ascending=False)
# print(bd)

#31
re = pd.DataFrame([
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Mouse", "price": 25}
])
re["quantity"] = re.groupby("name")["id"].transform("count")
# print(re)

#32
re["total_price"] = re["price"] * re["quantity"]
q = re.groupby("name")[["quantity", "total_price"]].sum().reset_index()
# print(q)

#33
y = pd.DataFrame([
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "T-Shirt", "price": 20, "category": "Clothing"}
])
y_filtered = y[y["category"] == "Electronics"]
# print(y_filtered)

#34
s = pd.DataFrame([
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Mouse", "category": "Electronics"},
    {"name": "Shirt", "category": "Clothing"}
])
res4 = s["category"].value_counts()
res4.columns = ["category", "count"]
# print(res4)

#35
s2 = pd.DataFrame([
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Mouse", "price": 25, "category": "Electronics"},
    {"name": "Shirt", "price": 20, "category": "Clothing"}
])
res5 = s2.groupby("category")["price"].mean()
res5.columns = ["category", "mean"]
# print(res5)

#36
s3 = pd.DataFrame([
    {"order_id": 101, "total_price": 1200},
    {"order_id": 102, "total_price": 50}
])
s3 = s3.sort_values("total_price", ascending=False)
# print(s3)

#37
s4 = pd.DataFrame([
    {"order_id": 101, "total_price": 1200},
    {"order_id": 102, "total_price": 50},
    {"order_id": 103, "total_price": 500},
    {"order_id": 104, "total_price": 1500}
])

s4 = s4.sort_values("total_price", ascending=False)[:3]
# print(s4)

#38
s_users = pd.DataFrame([
    {"user_id": 1, "user_name": "John"},
    {"user_id": 2, "user_name": "Alice"},
])
s_orders = pd.DataFrame([
    {"order_id": 101, "user_id": 1, "total_price": 1200},
    {"order_id": 102, "user_id": 2, "total_price": 50},
])
s5 = pd.merge(s_users, s_orders, on="user_id")
s5 = s5[["order_id", "user_name", "total_price"]]
# print(s5)

#39
s6 = pd.DataFrame([
    {"user_name": "John", "total_price": 1200},
    {"user_name": "John", "total_price": 500},
    {"user_name": "Alice", "total_price": 50},
])
res6 = s6.groupby("user_name")["total_price"].mean()
res6.columns = ["user_name", "mean_total"]
# print(res6)

#40
s7 = pd.DataFrame([
    {"user_name": "John", "order_id": 101},
    {"user_name": "John", "order_id": 103},
    {"user_name": "Alice", "order_id": 102}
])
res7 = s7.groupby("user_name")["order_id"].count()
res7.columns = ["user_name", "orders_count"]
# print(res7)

#41
s8 = pd.DataFrame([
    {"user_name": "John", "total_price": 1200},
    {"user_name": "John", "total_price": 500},
    {"user_name": "Alice", "total_price": 50},
])
res8 = s8.groupby("user_name")["total_price"].max()
res8.columns = ["user_name", "max_price"]
# print(res8)

#42
s9 = pd.DataFrame([
    {"user_name": "John", "category": "Electronics"},
    {"user_name": "John", "category": "Electronics"},
    {"user_name": "John", "category": "Clothing"},
    {"user_name": "Alice", "category": "Clothing"},
])
res9 = s9.groupby("user_name")["category"].nunique()
res9.columns = ["user_name", "unique_categories"]
# print(res9)

#43
s10 = pd.DataFrame([
    {"user_name": "John", "total_sum": 1700},
    {"user_name": "Alice", "total_sum": 25}
])
s10["VIP"] = s10["total_sum"] > 1000
# print(s10)

#44
s11 = pd.DataFrame([
    {"user_name": "John", "total_sum": 1700, "mean_total": 850},
    {"user_name": "Alice", "total_sum": 25, "mean_total": 25},
    {"user_name": "Bob", "total_sum": 1700, "mean_total": 600}
])
res11 = s11.sort_values(by=["total_sum", "mean_total"], ascending=[False, True])
# print(res11)

#45
s12 = pd.DataFrame([
    {"user_name": "John", "order_id": 101, "total_price": 1200, "category": "Electronics"},
    {"user_name": "John", "order_id": 103, "total_price": 500, "category": "Clothing"},
    {"user_name": "Alice", "order_id": 102, "total_price": 25, "category": "Clothing"}
])
res12 = s12.groupby("user_name").agg(
    total_orders=("order_id", "count"),
    total_sum=("total_price", "sum"),
    mean_total=("total_price", "mean"),
    max_order=("total_price", "max"),
    unique_categories=("category", "nunique")
)
res12["VIP"] = res12["total_sum"] > 1000
# print(res12)
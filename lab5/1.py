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
        return f"Product(id='{self.id}', name='{self.name}', category={self.category})"

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
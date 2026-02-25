import json
file = open("orders.json", "r", encoding="utf-8")
orders = json.load(file)
total_revenue = 0
for order in orders:
    total_revenue += order["total"]
users_orders = {}
for order in orders:
    user = order["user"]
    if user not in users_orders:
        users_orders[user] = 0
    users_orders[user] += 1
top_user = max(users_orders, key=users_orders.get)
total_items = 0
for order in orders:
    total_items += len(order["items"])
highest_order = orders[0]
for order in orders:
    if order["total"] > highest_order["total"]:
        highest_order = order
items_count = {}
for order in orders:
    for item in order["items"]:
        if item not in items_count:
            items_count[item] = 0
        items_count[item] += 1
create = open("summary.json", "x", encoding="utf-8")
summary = {
    "total_revenue": total_revenue,
    "top_user": highest_order["user"],
    "most_popular_item": items_count,
    "total_orders": len(orders)
}
json.dump(summary, create)
create.close()
#1
# a = [1,2,3,2,1]
# b = len(set(a))
# print(b)
from os import unsetenv

#2
# a = [1,3,2]
# b = [4,3,2]
# c = len(set(a) & set(b))
# print(c)

#3
# a = "python"
# b = "notebook"
# c = sorted(list(set(a) & set(b)))
# print(c)

#4
# math = {"Aida", "Nurlan", "Dana"}
# cs = {"Dana", "Aruzhan"}
# physics = {"Aida", "Serik"}
# a = (math ^ cs ^ physics) - (math & cs & physics)
# print(a)

#5
# python_group = {"Айгүл", "Бекзат", "Данияр"}
# java_group = {"Айгүл", "Самат", "Лаура"}
# a = python_group.intersection(java_group)
# print(a)
# b = python_group.difference(java_group)
# print(b)
# c = python_group | java_group
# print(c)

#6
# a = [
#     ("Ivanov", "paper"),
#     ("Petrov", "pens"),
#     ("Ivanov", "marker"),
#     ("Ivanov", "paper"),
#     ("Petrov", "envelope"),
#     ("Ivanov", "envelope")
# ]
# b = {}
# for k, v in a:
#     if k not in b:
#         b[k] = set()
#     b[k].add(v)
# for k, v in b.items():
#     print(f"{k}: {', '.join(sorted(v))}")

#7
# a = "Мен Python жақсы көремін және Python үйренемін"
# b = a.split()
# c = {}
# for i in b:
#     c[i] = c.get(i, 0) + 1
# print(c)

#8
# a = {"alma": 300, "banan": 450, "sut": 550}
# a.pop("alma")
# a.update({"et":700, "qarbyz":500, "qyryqqabat":250, "mai":150, "qiyar":250, "banan":450, "sut":550})
# for item in a:
#     if item in ["qarbyz", "banan"]:
#         a[item] *= 1.2
#     if item in ["et", "qyryqqabat", "mai", "qiyar", "sut"]:
#         a[item] *= 1.3
# for item, price in a.items():
#     print(f"{item} = {price}")

#9
# a = {"a": 95, "b": 70, "c": 55, "d": 32}
# b = max(a.values())
# c = min(a.values())
# for i, j in a.items():
#     if j == b:
#         print(i)
# for k, v in a.items():
#     if v == c:
#         print(k)
# print(sum(a.values())//len(a))

#10
# a = {'alma': 10, 'banan': 5, 'nan': 3}
# product, amount = 'banan', 3
# if product in a:
#     if a[product] >= amount:
#         a[product] -= amount
#         print(f"{product} сатып алынды. Қалғаны: {a[product]}")
#     else:
#         print(f"Жеткіліксіз! Қоймада {a[product]} ғана бар.")
# else:
#     print("Мұндай тауар жоқ.")
# product2, amount2 = 'banan', 6
# if product2 in a:
#     if a[product2] >= amount:
#         a[product2] -= amount
#         print(f"{product} сатып алынды. Қалғаны: {a[product]}")
#     else:
#         print(f"Жеткіліксіз! Қоймада {a[product]} ғана бар.")
# else:
#     print("Мұндай тауар жоқ.")
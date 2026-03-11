#1
# numbers = [1, 2, 3, 4, 5]
# a = list(map(lambda x: x*2, numbers))
# print(a)

#2
# words = ["кот", "машина", "арбуз", "дом"]
# res = list(map(lambda x: x.upper()+"!" if len(x)>3 else x.upper(), words))
# print(res)

#3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(filter(lambda x: x % 2 == 0, numbers))
# print(res)

#4
# numbers = [0, 5, 12, 7, 20, -3, 8]
# res = list(map(lambda x: x/2 if x % 2 == 0 else x*3, filter(lambda x: x > 5, numbers)))
# print(res)
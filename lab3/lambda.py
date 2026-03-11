#1
# func = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
# s = int(input())
# print(func(s))

#2
# func = lambda x: sorted(x, key=lambda s: (len(s), s))
# words = ["watermelon","cat", "car", "house", "pineapple"]
# print(func(words))

#3
# func = lambda x: list(filter(lambda s: s%2==0 and s>10, x))
# numbers = [5,12,7,20,33,8]
# print(func(numbers))

#4
# func = lambda s: list(
#     map(
#         lambda x: x**2 if x%2==0 else x*3, s
#     )
# )
# numbers = [1, 2, 3, 4, 5, 6]
# print(func(numbers))

#5
# func = lambda a,b: "a больше" if a > b else "b больше" if b > a else "равны"
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print(func(a,b))

#6
# numbers = [0, -3, 5, -7, 8]
# a = [(lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero")(x) for x in numbers]
# print(a)
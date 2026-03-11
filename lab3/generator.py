#1
# def even_numbers(n):
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             if i % 4 == 0:
#                 yield "кратно 4"
#             else:
#                 yield i
# n = int(input("Enter a number: "))
# for x in even_numbers(n):
#     print(x)

#2
# def filter_words(words):
#     for w in words:
#         if len(w) > 4:
#             if "а" in w:
#                 yield "c a"
#             else:
#                 yield w
# words = ["кот", "машина", "арбуз", "дом"]
# for w in filter_words(words):
#     print(w)

#3
# def infinite_numbers():
#     n = 1
#     while True:
#         if n % 3 == 0:
#             yield "Fizz"
#         elif n % 5 == 0:
#             yield "Buzz"
#         elif n % 3 == 0 and n % 5 == 0:
#             yield "FizzBuzz"
#         else:
#             yield n
#         n += 1
# a = infinite_numbers()
# b = int(input("Enter a number: "))
# for i in range(b):
#     print(next(a))

#4
# def squares(n):
#     for i in range(1,n+1):
#         if i**2 % 2 == 0:
#             yield "четный квадрат"
#         else:
#             yield i**2
# n = int(input("Enter a number: "))
# for i in squares(n):
#     print(i)
#1
# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             return False
#     return True
# def special_numbers(n):
#     for x in range(1, n+1):
#         if x % 3 == 0 and x % 5 == 0:
#             yield "FizzBuzz"
#         elif x % 3 == 0:
#             yield "Fizz"
#         elif x % 5 == 0:
#             yield "Buzz"
#         elif is_prime(x):
#             yield "Простое"
#         else:
#             yield x
# for j in special_numbers(20):
#     print(j)

#2
# words = ["кот", "машина", "арбуз", "дом", "ананас"]
# res = [(lambda x: (w.upper() if len(w)>4 else "short")+("*" if "а" in w else ""))(w) for w in words]
# print(res)

#3
# def process_numbers(numbers):
#     for x in filter(lambda x: x>=0, numbers):
#         res = (x/2 if x %2==0 else x*3+1)
#         yield res
# numbers = [5, -2, 8, 0, -7, 3]
# for j in process_numbers(numbers):
#     print(j)

#4
# students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
# res = {
#     name: (lambda s: "Отлично" if s >= 90 else "Хорошо" if 70 <= s < 90 else "Удовлетворительно")(score)
#     for name, score in students
# }
# print(res)

#5
# def matrix_transform(matrix):
#     for row in matrix:
#         for i in row:
#             if i % 2 == 0 and i % 3 == 0:
#                 yield "Кратно 6"
#             elif i % 3 == 0:
#                 yield "Кратно 3"
#             elif i % 2 == 0:
#                 yield "Четное"
#             else:
#                 yield i
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for j in matrix_transform(matrix):
#     print(j)
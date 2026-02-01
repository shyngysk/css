#1
# a = int(input("Enter a number: "))
# b=0
# for i in range(1, a+1):
#     if i % 2 !=0:
#         b += i**2
# print(b)

#2
# a = int(input("Enter a number: "))
# b = a
# c = 0
# while a > 0:
#     d = a%10
#     c = c*10 + d
#     a = a//10
# if b == c:
#     print("Палиндром")
# else:
#     print("Палиндром емес")

#3
# a = int(input("Enter a number: "))
# count = 0
# i = 1
# while i <= a:
#     if a % i == 0:
#         count += 1
#     i += 1
# print(count)

#4
# a = int(input("Enter a number: "))
# b = 1
# c = 0
# while a > 0:
#     d = a % 10
#     if d % 2 ==1:
#         b *= d
#         c += 1
#     a = a // 10
# if c == 0:
#     print(0)
# else:
#     print(b)

#5
# a = int(input("Enter a number: "))
# b = 0
# while a != 0:
#     b += a
#     a = int(input("Enter a number: "))
# print(b)

#6
# a = int(input("Enter count of numbers: "))
# b = int(input("Enter a number: "))
# min = b
# max = b
# for i in range(a-1):
#     c = int(input("Enter another number: "))
#     if c < min:
#         min = c
#     if c > max:
#         max = c
# print("Minimum: ", min)
# print("Maximum: ", max)

#7
# a = 0
# b = 1
# while a <= 100:
#     a += b
#     b += 1
# print("Тоқтаған сан: ", b - 1)
# print("Қосынды: ", a)

#8
# a = input("Enter a text: ")
# b = input("Enter a symbol: ")
# count = 0
# for i in a:
#     if i == b:
#         count += 1
# print(count)

#9
# N = int(input("Enter a number: "))
# sum = 0
# for i in range(1, N+1):
#     print(i, end=" ")
#     sum += i
# print(sum)

#10
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "*", i, "=", n*i)
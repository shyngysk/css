# def a(nums):
#     max1 = nums[0]
#     max2 = nums[1]
#     for i in nums:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif i < max1 and i > max2:
#             max2 = i
#     return max2
# print(a([4, 7, 1, 9, 3, 9, 5]))
from http.cookiejar import uppercase_escaped_char
from random import vonmisesvariate

# def main(text):
#     d = {}
#     for i in text:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d
# print(main("programming"))

# def a(nums):
#     a = []
#     b = []
#     for i in nums:
#         if i % 2 == 0:
#             a.append(i)
#         else:
#             b.append(i)
#     return a, b
# print(a([1, 2, 3, 4, 5, 6, 7, 8]))

# def a(nums):
#     a = []
#     for i in nums:
#         if i < 2:
#             continue
#         is_prime = True
#         for n in range(2, i):
#             if i % n == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             a.append(i)
#     return a
# print(a([3, 4, 5, 6, 7, 8]))

# def a(text):
#     prev = text[0]
#     c = 1
#     res = ""
#     for ch in text:
#         if ch == prev:
#             c = c + 1
#         else:
#             res += prev + str(c)
#             prev = ch
#             c = 1
#     return res
# print(a("aabbbcdddeee"))

# s = "python"
# res = ""
# for i in range (len(s)):
#     if i % 2 != 0:
#         res += s[i].upper()
#     else:
#         res += s[i].lower()
# print(res)

# text = "He11o_W0rld!! 2025 :)"
# res = ""
# for i in text:
#     if isinstance(i, str):
#         res += i.lower()
# print(res)

# text = "p@y#t%h^o&n"
# res = ""
# for i in text:
#     if i.isalnum():
#         res += i
# print(res)

# words = ["apple", "hi", "banana", "cat", "elephant"]
# a = []
# for word in words:
#     if len(word)>5:
#         a.append(word)
# print(a)

# grades = {"Math": 78, "Physics": 92, "English": 85}
# for key, value in grades.items():
#     if value >= 90:
#         grades[key]= "A"
#     if 89>value>80:
#         grades[key]= "B"
#     if value<80:
#         grades[key]= "C"
# print(grades)

# def list(a):
#     if 2 and 9 in a:
#         return "OK"
#     return "NO"
# print(list([5, 8, 2, 9, 1, 7]))
#1
# nums = [4, 9, 1, 7, 3]
# a = sorted(nums)
# b = a[-1] - a[0]
# print(b)
#2
# text = "education"
# a = "aeiouyAEIOUY"
# c = 0
# for letter in text:
#     if letter in a:
#         c += 1
# print(c)
#3
# data = {"a": 10, "b": 3, "c": 25, "d": 7}
# max = 0
# for v in data.values():
#     if v > max:
#         max=v
# for k in data.keys():
#     if data[k] == max:
#         print(k)
#4
# nums = [1, 2, 3, 4, 5]
# a = []
# for num in nums:
#     if num % 2 != 0:
#         a.append(num**2)
# print(a)
#5
# def d(a):
#     for i in a:
#         if a[i] == a[i+1] or a[i] == a[i-1]:
#             return "YES"
#     return "NO"
# print(d([1, 2, 2, 3, 4]))


#1
# nums = [12, 3, 5, 8, 7, 20, 15]
# a = []
# for i in nums:
#     if i<5:
#         a.append(i)
#     elif i>10:
#         a.append(i)
# print(a)

#3
# scores = {"Aruzhan": 85, "Daniyar": 92, "Mira": 74, "Erzat": 90}
# max = 0
# min = 0
# for k, v in scores.items():
#     if v > max:
#         max = v
#     elif v < min:
#         min = v
#     elif scores[k] == max:
#         print("max:", k)
#     elif scores[k] == min:
#         print("min:", k)

#4
# def m(nums):
#     a = []
#     for i in nums:
#         if i < 2:
#             continue
#             prime=True
#             for j in range(2, i):
#                 if i % j == 0:
#                     prime=False
#                     break
#             if prime:
#                 a.append(i)
#     return a
# print(m([2, 3, 4, 5, 6, 7, 8]))

#5
# text = "banana"
# freq = {}
# for letter in text:
#     if letter in freq:
#         freq[letter] += 1
#     else:
#         freq[letter] = 1
# print(freq)
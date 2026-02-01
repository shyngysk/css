# bagalar = {"a":56, "b":87, "c":90, "d":10}
# g = sum(bagalar.values())//len(bagalar)
# print(g)
# for k, v in bagalar.items():
#     if v > g:
#         print(k, v)

# a = {"алма": 3, "банан": 5, "апельсин": 2}
# b = {"банан": 4, "алма": 1, "киви": 7}
#
# # Біріктіру және мәндерін қосу
# birik = a.copy()  # a сөздігін көшіріп аламыз
#
# for k, v in b.items():
#     birik[k] = birik.get(k, 0) + v  # егер кілт бар болса, мәнін қосамыз
#
# print(birik)

# a = input()
# b = list(map(int, a.split()))
# c = 1
# max = 1
# for i in range(0,len(b)):
#     if b[i] == b[i-1]:
#         c += 1
#         max = c
#     else:
#         c = 1
# print(max)

# a = input()
# b = list(map(int, a.split()))
# max = 0
# maxx = 0
# for i in b:
#     if i > max:
#         maxx = max
#         max = i
# print(maxx)

# a = input()
# r = ""
# for i in a:
#     if i.isdigit():
#         r += "0"
#     else:
#         r += i
# print(r)

#1
# a = list(input().split())
# c = 1
# max = 1
# for i in range(0, len(a)):
#     if a[i] == a[i-1]:
#         c += 1
#         max = c
#     else:
#         c = 1
# print(max)

#2
# a = input()
# b = ""
# for i in a:
#     if i.isdigit():
#         b += "0"
#     else:
#         b += i
# print(b)

#3
# def m(a):
#     b = list(map(int, a.split()))
#     max1 = 0
#     max2 = 0
#     for i in b:
#         if i > max1:
#             max2 = max1
#             max1 = i
#     return max2
# print(m(input()))

#5
# a = input()
# b = list(map(input, a.split()))
# s = ""
# for i in b:
#     if i.isalpha():
#         s += i
# print(s)

#6
# a = list(map(int, input().split()))
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

#8
# a = input()
# b = a.lower()
# if b == b[::-1]:
#     print("YES")
# else:
#     print("NO")

#9
# a = list(map(int, input().split()))
# max1 = 0
# max2 = 0
# min = a[0]
# for i in a:
#     if i > max1:
#         max2 = max1
#         max1 = i
#     if i < min:
#         min = i
# print("max:", max1)
# print("min:", min)
# print("second max:", max2)


#2
# a = input()
# b = ""
# for i in a:
#     if i.isalpha():
#         b += "x"
#     else:
#         b += i
# print(b)

#3
# a = list(map(int, input().split()))
# m1 = 0
# m2 = 0
# m3 = 0
# for i in a:
#     if i > m1:
#         m3 = m2
#         m2 = m1
#         m1 = i
# print(m3)

#4
# a = list(map(int, input().split()))
# max = 0
# for i in a:
#     if i > max:
#         max = i
# print(max)

#5
# a = input()
# b = ""
# for i in a:
#     if i.isdigit():
#         b += i
# print(b)

#7
# a = int(input())
# c = 0
# while a>0:
#     c += a%10
#     a//=10
# print(c)

#8
# a = input()
# b = input()
# if sorted(a) == sorted(b):
#     print("YES")
# else:
#     print("NO")

#9
# a = list(map(int, input().split()))
# max = a[0]
# for i in range(0, len(a)):
#     if a[i] < max:
#         print(i)

#10
# a = input()
# b = ""
# for i in a:
#     if i.isalnum():
#         b += i
# print(b)

#a1
# def countdigits(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n//=10
#     return count
# print(countdigits(507294))

#a2
# def is_pal(n):
#     if n == n[::-1]:
#         return True
#     return False
# print(is_pal(input()))

#a3
# def second_max(a):
#     m1 = 0
#     m2 = 0
#     b = list(map(int, a.split()))
#     for i in b:
#         if i > m1:
#             m2 = m1
#             m1 = i
#     return m2
# print(second_max(input()))

#a4
# def replace_letters(s):
#     b = ""
#     for i in s:
#         if i.isalpha():
#             b += "x"
#         else:
#             b += i
#     return b
# print(replace_letters(input()))

#b1
# def linear_search(a, x):
#     for i in range(0, len(a)):
#         if a[i] == x:
#             return "YES"
#     return None
# print(linear_search([1, 2, 3, 4, 5], 5))

#b2
# def ls(a):
#     b = list(map(int, a.split()))
#     idx = 0
#     min = b[0]
#     for i in range(0, len(b)):
#         if b[i] < min:
#             min = b[i]
#             idx = i
#     return idx
# print(ls(input()))

#b3
# def binary_search(a, x):
#     low = 0
#     high = len(a) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if a[mid] == x:
#             return mid
#         elif a[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
# print(binary_search([1, 2, 3, 4, 5], 5))

#1
# def second_max(a):
#     b = list(map(int, a.split()))
#     m1 = 0
#     m2 = 0
#     for i in range(0, len(b)):
#         if b[i] > m1:
#             m2 = m1
#             m1 = b[i]
#         elif m1 > b[i] > m2:
#             m2 = b[i]
#     return m2
# print(second_max(input()))

#2
# a = list(map(int, input().split()))
# c = 1
# m = 0
# for i in range(0, len(a)):
#     if a[i] == a[i-1]:
#         c += 1
#     else:
#         c = 1
#     if c > m:
#         m = c
# print(m)

#3
# a = list(map(int, input().split()))
# for i in a:
#     if i % 2 != 0:
#         a.remove(i)
# print(a)

#4
# def linear_search(a, x):
#     for i in range(0, len(a)):
#         if a[i] == x:
#             return "YES"
#     return "NO"
# print(linear_search([1, 2, 3, 4, 5], 5))

#5
# a = list(map(int, input().split()))
# m = a[0]
# idx = 0
# for i in range(0, len(a)):
#     if a[i] < m:
#         m = a[i]
#         idx = i
# print(idx)

#6
# def binary_search(a, x):
#     low = 0
#     high = len(a) - 1
#     while high >= low:
#         mid = (high + low) // 2
#         if a[mid] == x:
#             return mid
#         elif a[mid] < x:
#             low = mid + 1
#         else:
#             high = mid -1
#     return mid
# print(binary_search([1, 3, 5, 7, 9, 11, 13, 15], 11))

#7
# def bubble(a):
#     b = list(map(int, a.split()))
#     for i in range(len(b)):
#         for j in range(len(b) - i - 1):
#             if b[j] > b[j + 1]:
#                 b[j], b[j + 1] = b[j + 1], b[j]
#     return b
# print(bubble(input()))

#9
# def a(b):
#     c = 0
#     while b > 0:
#         c += b%10
#         b = b//10
#     return c
# print(a(int(input())))

#10
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(int(input())))

#11
# a = list(map(int, input().split()))
# min1 = min2 = a[0]
# for i in range(0, len(a)):
#     if a[i] < min1:
#         min2 = min1
#         min1 = a[i]
# print(min2)

#a1
# a = list(map(int, input().split()))
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(*b)

#a3
# a = list(map(int, input().split()))
# b = []
# m1 = m2 = a[0]
# for i in range(0, len(a)):
#     if a[i] > m1:
#         m2 = m1
#         m1 = a[i]
#     elif m1 > a[i] > m2:
#         m2 = a[i]
# b.append(m1)
# b.append(m2)
# print(*b)

#a4
# a = list(map(int, input().split()))
# for i in a:
#     if i == 0:
#         a.remove(0)
#         a.append(0)
# print(*a)

#b1
# def l(a):
#     x = int(input())
#     b = list(map(int, a.split()))
#     c = 0
#     for i in b:
#         if i == x:
#             c += 1
#     return c
# print(l(input()))

#b2
# def q(a):
#     x = int(input())
#     b = list(map(int, a.split()))
#     low = 0
#     high = len(b) - 1
#     while high >= low:
#         mid = (low + high) // 2
#         if b[mid] == x:
#             return mid
#         elif b[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#         if b[mid] - b[low] < b[high] - b[mid]:
#             return b[low]
#         else:
#             return b[high]
#     return -1
# print(q(input()))

#c1
# def bubble(a):
#     c = 0
#     b = list(map(int, a.split()))
#     for i in range(len(b)):
#         swapped = False
#         for j in range(len(b) - i - 1):
#             if b[j] > b[j + 1]:
#                 b[j], b[j + 1] = b[j + 1], b[j]
#                 swapped = True
#                 c += 1
#         return "Swaps:", c
#         if not swapped:
#             break
#     return "Sorted:", b
# print(bubble(input()))

#d1
# def sum(a):
#     b = list(map(int, a.split()))
#     c = 0
#     for i in b:
#         c += i
#     return c
# print(sum(input()))

#d2
# def power(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a**b
# print(power(int(input()), int(input())))

#e1
# def negr(loh):
#     hui = list(map(int, loh.split()))
#     c = 1
#     max = 0
#     for i in range(1, len(hui)):
#         if hui[i] == hui[i-1]:
#             c += 1
#         else:
#             c = 1
#         if c > max:
#             max = c
#     return max
# print(negr(input()))

#e2
# def pal(a):
#     b = list(map(int, a.split()))
#     if b == b[::-1]:
#         return "YES"
#     return "NO"
# print(pal(input()))

#1
# a = input().split()
# d = {}
# for i in a:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# max = 0
# b = ""
# for i in a:
#     if d[i] > max:
#         max = d[i]
#         b = i
# print(b)

#2
# a = list(map(int, input().split()))
# c = 1
# max = 0
# int = 0
# for i in range(1, len(a)):
#     if a[i] == a[i-1]:
#         c += 1
#         int = a[i]
#     else:
#         c = 1
#     if c > max:
#         max = c
# print(int)

#3
# a = input().split()
# c = {}
# for i in a:
#     if i in c:
#         c[i] = c[i] + 1
#     else:
#         c[i] = 1
# min = len(a)
# b = ""
# for i in a:
#     if c[i] < min:
#         min = c[i]
#         b = i
# print(b)

#4
# a = input().split()
# b = {}
# for i in a:
#     if i in b:
#         b[i] = b[i] + 1
#     else:
#         b[i] = 1
# print(b)

#1
# a = list(map(int, input().split()))
# c = 0
# max = a[0]
# min = a[0]
# for i in a:
#     c += i
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(c, max, min)

#2
# a = list(map(int, input().split()))
# b = tuple(a)
# print(b)

#3
# a = list(map(int, input().split()))
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# c = len(b)
# print(c)

#4
# a = list(map(int, input().split()))
# b = {}
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# max = 0
# c = ""
# for i in a:
#     if b[i] > max:
#         max = b[i]
#         c = i
# print(c)

#5
# def a(b):
#     c = ""
#     for i in b:
#         if i.isalpha():
#             c += i
#         else:
#             c += "0"
#     return c
# print(a(input()))

#7
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

#8
# def l(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1
# print(l(list(map(int, input().split())), int(input())))

#9
# def b(a, x):
#     low = 0
#     high = len(a) - 1
#     while high >= low:
#         mid = (high + low)//2
#         if a[mid] == x:
#             return mid
#         elif a[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
# print(b(list(map(int, input().split())), int(input())))

#10
# a = list(map(int, input().split()))
# for i in range(len(a)):
#     for j in range(len(a)-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(*a)

#11
# a = list(map(int, input().split()))
# for i in range(len(a)):
#     print(a[(len(a)-1)//2])
#     break

#12
# b = input().split()
# c = {}
# for i in b:
#     if i in c:
#         c[i] += 1
#     else:
#         c[i] = 1
# first = True
# for i in b:
#     if i in c:
#         if not first:
#             print(" ", end="")
#         print(i, ":", c[i], sep="", end="")
#         first = False
#         del c[i]

#1
# a = list(map(int, input().split()))
# c = 0
# max = a[0]
# min = a[0]
# for i in a:
#     c += i
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(c, max, min)

#2
# a = input()
# c = ""
# for i in a:
#     if i.isalpha():
#         c += i
#     else:
#         c += "0"
# print(c)

#3
# a = input().split()
# b = {}
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# max = 0
# c = ""
# for i in a:
#     if b[i] > max:
#         max = b[i]
#         c = i
# print(c)

#4
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(int(input())))

#5
# def binary(a, x):
#     low = 0
#     high = len(a) - 1
#     while high >= low:
#         mid = (high + low) // 2
#         if a[mid] == x:
#             return mid
#         elif a[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# print(binary(list(map(int, input().split())), int(input())))

def analyze_text(text):
    text = text.lower()
    c = ""
    for i in text:
        if i.isalpha():
            c += i
        else:
            c += " "
    vowels = 'aeiou'
    unique = set()
    for i in c:
        if i in vowels:
            unique.add(i)
    v_c = len(unique)
    w = c.split()
    res = []
    seem = set()
    for a in w:
        if len(a) >= 5 and a[0] == a[-1] and a not in seem:
            res.append(a)
            seem.add(a)
    return (v_c, " ".join(res))
print(analyze_text(input()))
#LIST AND STRING
#1
# def analyze_text(text):
#     text = text.lower()
#     c = ""
#     for i in text:
#         if i.isalpha():
#             c += i
#         else:
#             c += ""
#     vowels = 'aieuo'
#     unique_vowels = set()
#     for i in c:
#         if i in vowels:
#             unique_vowels.add(i)
#     v_count = len(unique_vowels)
#     words = c.split()
#     res = []
#     seen = set()
#     for b in words:
#         if len(b) >= 5 and b[0] == b[-1] and b not in seen:
#             res.append(b)
#             seen.add(b)
#     return (v_count, " ".join(res))
# print(analyze_text("LeVeL!2"))
from unittest import result


#2
# function = lambda s: " ".join(
#     map(
#         lambda x: x[::-1],
#         filter(
#             lambda x: x.isalpha() and len(x) % 2 == 0,
#             s.split()
#         )
#     )
# )
# text = input()
# print(function(text))

#3
# def top_k_words(text, k):
#     text = text.lower()
#     c = ""
#     for i in text:
#         if i.isalpha() or i == " ":
#             c += i
#         else:
#             c += " "
#     words = c.split()
#     count = {}
#     for word in words:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
#     items = list(count.items())
#     items.sort(key=lambda x: (-x[1], x[0]))
#     top_k = [item[0] for item in items[:k]]
#     return top_k
# text = input()
# print(top_k_words(text, int(input())))

#4
# f = lambda s: " ".join(
#     w.lower() for w in s.split()
#     if sum(1 for ch in w if ch.isupper()) == 1
#     and not w[0].isupper()
#     and not w[-1].isdigit()
# )
# text = input()
# print(f(text))

#5
# def compress_text(text):
#     if not text:
#         return ""
#     result = ""
#     current = text[0]
#     count = 1
#     for i in range(1, len(text)):
#         if text[i].lower() == current.lower():
#             count += 1
#         else:
#             if count == 1:
#                 result += current
#             else:
#                 result += current + str(count)
#             current = text[i]
#             count = 1
#     if count == 1:
#         result += current
#     else:
#         result += current + str(count)
#     return result
# print(compress_text("aaBBcDD"))

#6
# words = lambda s: list(
#     filter(
#         lambda i: len(i) >= 4 and i.isalpha() and len(set(i)) == len(i),
#         s.split()
#     )
# )
# text = input()
# print(words(text))

#7
# def palindrome_words(text):
#     text = text.lower()
#     c = ""
#     for i in text:
#         if i.isalpha():
#             c += i
#         else:
#             c += " "
#     d = c.split()
#     res = []
#     for j in d:
#         if len(j) >= 3 and j == j[::-1] and j not in res:
#             res.append(j)
#     for k in range(len(res)):
#         for v in range(k+1, len(res)):
#             if len(res[v]) > len(res[k]):
#                 res[k], res[v] = res[v], res[k]
#             elif len(res[v]) == len(res[k]) and res[v] < res[k]:
#                 res[k], res[v] = res[v], res[k]
#     return res
# text = input()
# print(palindrome_words(text))

#8
# func = lambda s: " ".join(
#     map(
#         lambda x: x if any(i.isdigit() for i in x)
#         else ("VOWEL" if x[0].lower() in "aeiou" else "CONSONANT"),
#         s.split()
#     )
# )
# text = input()
# print(func(text))

#9
# def alt_text(text, n):
#     res = ""
#     idx = 0
#     for i in range(0, len(text), n):
#         block = text[i:i+n]
#         if idx % 2 == 0:
#             res += block.upper()
#         else:
#             res += block.lower()
#         idx += 1
#     return res
# text = input()
# n = int(input())
# print(alt_text(text, n))

#10
# count = lambda s: sum(
#     1 for i in s.split()
#     if any(ch.isdigit() for ch in i)
#     and not i[0].isdigit()
#     and len(i) >= 5
# )
# text = input()
# print(count(text))

#11
# def common_unique_chars(s1, s2):
#     a = ""
#     b = set()
#     for i in s1:
#         if not i.isalpha():
#             continue
#         if i in b:
#             continue
#         if i in s2:
#             a += i
#             b.add(i)
#     return a
# s1 = input()
# s2 = input()
# print(common_unique_chars(s1, s2))

#12
# func = lambda s: list(
#     filter(
#         lambda x: len(x) >= 3 and x[0] == x[-1] and not x == x[::-1] and x.isalpha(),
#         s.split()
#     )
# )
# text = input()
# print(func(text))

#13
# def replace_every_nth(text, n, char):
#     a = ""
#     b = text.split()
#     idx = 0
#     for i in b:
#         for j, ch in enumerate(i):
#             if len(i) >= 3 and (idx + 1) % n == 0:
#                 if not ch.isdigit():
#                     a += char
#                 else:
#                     a += ch
#             else:
#                 a += ch
#             idx += 1
#         a += " "
#         idx += 1
#     return a.rstrip()
# text = input("Enter a sentence: ")
# n = int(input("Enter a number: "))
# char = input("Enter a character: ")
# print(replace_every_nth(text, n, char))

#14
# func = lambda s: ",".join(
#     filter(
#         lambda x: len(set(x)) > 3 and len([ch for ch in x.lower() if ch in "aeiou"]) == len(set(ch for ch in x.lower() if ch in "aeiou")),
#         s.split()
#     )
# )
# text = input()
# print(func(text))

#15
# def word_pattern_sort(text):
#     vowels = "aeuio"
#     words = text.lower().split()
#     gr = {}
#     for i in words:
#         a = len(i)
#         if a not in gr:
#             gr[a] = []
#         gr[a].append(i)
#     res = []
#     lens = list(gr.keys())
#     lens.sort()
#     for b in lens:
#         gr = gr[b]
#         gr.sort(key=lambda x: (-sum(-1 for c in x if c in vowels), x))
#         res.extend(gr)
#     return res
# print(word_pattern_sort("hello world"))

#16
# def transform_list(nums):
#     a = list(map(int, nums.split()))
#     b = []
#     d = []
#     c = 0
#     for i in a:
#         if i >= 0:
#             b.append(i)
#     for j in b:
#         if j % 2 != 0 and j > 10:
#             while j > 0:
#                 c += j%10
#                 j //= 10
#             d.append(c)
#             c -= c
#         elif j % 2 == 0:
#             d.append(j**2)
#         else:
#             d.append(j)
#     return d
# print(transform_list(input()))

#17
# func = lambda s: list(
#     map(
#         lambda x: x**2,
#         filter(
#             lambda x: (x % 3 == 0 or x % 5 == 0) and x % 15 != 0 and len(str(abs(x))) % 2 == 1,
#             s
#         )
#     )
# )
# text = [3, 4, 5, 15, 33, 105]
# print(func(text))

#18
# def flatten_and_filter(lst):
#     res = []
#     for i in lst:
#         if type(i) == list:
#             res += flatten_and_filter(i)
#         else:
#             res.append(i)
#     a = []
#     for j in res:
#         if j > 0 and j % 4 != 0 and len(str(abs(j))) > 1:
#             a.append(j)
#     b = sorted(a)
#     return b
# print(flatten_and_filter([12, 32, 55, 3, 7, [112, 456, 999]]))

#19
# func = lambda a, b: [x for x, y in zip(a, b) if x == y and x % 2 == 0]
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(func(a, b))

#20
# def max_subarray_sum(nums, k):
#     max = None
#     for i in range(len(nums) - k + 1):
#         a = nums[i:i + k]
#         if all(x > 0 for x in a):
#             b = sum(a)
#             if max is None or b > max:
#                 max = b
#     return max
# print(max_subarray_sum(list(map(int, input().split())), int(input())))

#21
# func = lambda s: [x.upper() for x in s if x.isalpha() and len(x) > 4 and len(set(x)) == len(x)]
# text = ["hello", "world"]
# print(func(text))

#22
# def group_by_parity_and_sort(nums):
#     a = list(map(int, nums.split()))
#     b = []
#     c = []
#     for i in a:
#         if i % 2 == 0:
#             b.append(i)
#         else:
#             c.append(i)
#     d = sorted(b) + sorted(c)
#     return d
# print(group_by_parity_and_sort(input()))

#23
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if i % n == 0:
#             return False
#     return True
# func = lambda x: [j for i, j in enumerate(x)
#                   if is_prime(i) and j % 2 == 1 and j > sum(x)/len(x)]
# numbers = [10, 3, 5, 7, 2, 9]
# print(func(numbers))

#24
# def longest_increasin_sublist(nums):
#     longest = []
#     current = [nums[0]]
#     for i in range(1, len(nums)):
#         if nums[i] > nums[i-1]:
#             current.append(nums[i])
#         else:
#             if len(current) > len(longest):
#                 longest = current
#             current = [nums[i]]
#     if len(current) > len(longest):
#         longest = current
#     return longest
# print(longest_increasin_sublist(list(map(int, input().split()))))

#25
# func = lambda x: list(
#     map(lambda i: sum(i)/len(i),
#         filter(lambda i: len(i) >= 3 and sum(i) % 2 == 0, x)
#     )
# )
# a = [[1,2,3], [4,5], [6,7,8], [1,1,1]]
# print(func(a))

#26
# def remove_duplicates_keep_last(nums):
#     a = []
#     res = []
#     for i in range(len(nums)-1, -1, -1):
#         if nums[i] not in a:
#             a.append(nums[i])
#             res.append(nums[i])
#     res.reverse()
#     return res
# print(remove_duplicates_keep_last(list(map(int, input().split()))))

#27
# func = lambda x: sorted(x, key=lambda i: (-len(i), i))[:5]
# text = ["apple", "cat", "banana", "dog", "elephant", "ant"]
# print(func(text))

#28
# def moving_average(nums, k):
#     res = []
#     for i in range(len(nums) - k + 1):
#         a = nums[i:i + k]
#         b = True
#         for j in a:
#             if j < 0:
#                 b = False
#                 break
#         if b:
#             c = sum(a)/k
#             res.append(c)
#     return res
# print(moving_average(list(map(int, input().split())), int(input())))

#29
# func = lambda a, b: list(
#     filter(lambda x: x not in b and x > sum(a)/len(a), a)
# )
# a = [10, 5, 8, 3, 12]
# b = [5, 3]
# print(func(a, b))

#30
# def analyze_strings_list(words):
#     a = []
#     for i in words:
#         digit = False
#         for j in i:
#             if j.isdigit():
#                 digit = True
#                 break
#         if digit:
#             continue
#         if len(i) % 2 == 0:
#             b = i[::-1]
#         else:
#             b = i.upper()
#         if b not in a:
#             a.append(b)
#     return a
# words = ["apple", "cat1", "dog", "moon", "sun", "dog"]
# print(analyze_strings_list(words))

#DICT AND SET
#1
# def invert_unique(d):
#     a = {}
#     for k, v in d.items():
#         if v not in a:
#             a[v] = []
#         if k not in a[v]:
#             a[v].append(k)
#     return a
# d = {"a":1, "b":2, "c":1}
# print(invert_unique(d))

#2
# a = lambda s: set(
#     filter(lambda x: x > sum(s)/len(s) and x % 2 == 1 and x % 5 != 0, s)
# )
# x = {3,10,7,15,9,20}
# print(a(x))

#3
# def merge_dict_sum(a, b):
#     c = {}
#     for k in a:
#         c[k] = a[k]
#     for k in b:
#         if k in c:
#             c[k] += b[k]
#         else:
#             c[k] = b[k]
#     return c
# a = {"a":2, "b":5}
# b = {"b":7, "c":8}
# print(merge_dict_sum(a,b))

#4
# def filter_sets(sets_list):
#     a = []
#     for i in sets_list:
#         if len(i) <= 3:
#             continue
#         negative = False
#         even = False
#         for j in i:
#             if j < 0:
#                 negative = True
#             if j % 2 != 0:
#                 even = True
#         if not negative and even:
#             a.append(i)
#     return a
# sets_list = [{1,2,3,4}, {1,-2,3}, {5,7,9,11}, {2,4,6,8}]
# print(filter_sets(sets_list))

#5
# a = lambda b: sorted(b.keys(), key=lambda x: (-b[x], x))[:5]
# b = {"apple": 5, "banana": 2, "orange": 5, "pear": 1, "kiwi": 7, "plum": 7}
# print(a(b))

#6
# def deep_sum(d):
#     total = 0
#     for v in d.values():
#         if isinstance(v, int):
#             total += v
#         elif isinstance(v, list):
#             for i in v:
#                 total += i
#         elif isinstance(v, dict):
#             total += deep_sum(v)
#     return total
# d = {
#     "a": 1,
#     "b": [2, 3],
#     "c": {
#         "d": 4,
#         "e": [5, 6],
#         "f": {"g": 7}
#     }
# }
# print(deep_sum(d))

#7
# f = lambda a, b: set(
#     filter(
#         lambda x: x % 2 == 0, a ^ b
#     )
# )
# a = {2, 3, 4, 5}
# b = {4, 5, 6, 7}
# print(f(a, b))

#8
# def sort_dict_by_value_length(d):
#     a = list(d.items())
#     a.sort(key=lambda x: (len(x[1]), x[0]))
#     return a
# d = {"apple": "red", "banana": "yellow", "kiwi": "green", "pear": "red"}
# print(sort_dict_by_value_length(d))

#9
# def common_elements_all(sets_list):
#     if not sets_list:
#         return set()
#     a = sets_list[0].copy()
#     for i in sets_list[1:]:
#         b = set()
#         for j in a:
#             if j in i:
#                 b.add(j)
#         a = b
#     return a
# sets_list = [{1,2,3}, {2,3,4}, {3,2,5}]
# print(common_elements_all(sets_list))

#10
# func = lambda s: {
#     k: sorted(filter(lambda a: a % 2 == 1, v))
#     for k, v in s.items()
#     if list(filter(lambda a: a % 2 == 1, v))
# }
# d = {
#     "a": [1,2,3,4],
#     "b": [2,4,6],
#     "c": [5,7,1]
# }
# print(func(d))

#11
# def group_by_length(words):
#     group = {}
#     for word in words:
#         length = len(word)
#         if length in group:
#             group[length].append(word)
#         else:
#             group[length] = [word]
#     return group
# print(group_by_length(["cat", "dog", "apple", "car", "dog", "banana"]))

#12
# func = lambda s: set(
#     filter(
#         lambda x: x.isalpha() and len(x) > 4 and len(set(x)) == len(x),
#         s
#     )
# )
# st = {"apple", "plane", "dog12", "world", "abcde", "letter"}
# print(func(st))

#13
# def invert_dict_strict(d):
#     inverse = {}
#     for k, v in d.items():
#         inverse[v] = k
#         if v in inverse:
#             inverse[v] = inverse[v]
#     return inverse
# d = {'a': 1, 'b': 2, 'c': 2, 'd': 4}
# print(invert_dict_strict(d))

#14
# def top_k_frequent(nums, k):
#     a = {}
#     for i in nums:
#         if i in a:
#             a[i] += 1
#         else:
#             a[i] = 1
#     b = set()
#     for _ in range(k):
#         if not a:
#             break
#         maxx = None
#         maxc = -1
#         for num in a:
#             if a[num] > maxc or (a[num] == maxc and num<maxc):
#                 maxx = a[num]
#                 maxc = num
#         b.add(maxx)
#         del a[maxc]
#     return b
# print(top_k_frequent([1,2,3,4,5,6,7,8,9], 2))

#15
# func = lambda s: {
#     k: v
#     for k, v in s.items()
#     if v > (sum(s.values())/len(s.values())) and v % 2 == 1
# }
# d = {"a":5, "b":2, "c":9, "d":4}
# print(func(d))

#16
# def update_counts(d, items):
#     for item in items:
#         if item in d:
#             d[item] += 1
#         else:
#             d[item] = 1
#     return d
# d = {"apple": 2, "banana": 1}
# items = ["apple", "orange", "apple", "banana"]
# print(update_counts(d, items))

#17
# func = lambda x, y, z: (a&b) - c
# a = {1,2,3,4}
# b = {3,4,5}
# c = {4}
# print(func(a, b, c))

#18
# def sort_dict_by_value_sum(d):
#     a = []
#     for k in d:
#         b = 0
#         for v in d[k]:
#             b += v
#         a.append((k, b))
#     c = len(a)
#     for i in range(c):
#         for j in range(i + 1, c):
#             k1, s1 = a[i]
#             k2, s2 = a[j]
#             if s2 > s1 or (s1 == s2 and k1 > k2):
#                 a[i], a[j] = a[j], a[i]
#     return a
# d = {
#     "a": [1,2,3],
#     "b": [5],
#     "c": [2,2,2]
# }
# print(sort_dict_by_value_sum(d))

#19
# def filter_by_digit_sum(nums):
#     res = set()
#     for num in nums:
#         sum = 0
#         if num % 2 == 0:
#             continue
#         else:
#             for i in str(num):
#                 sum += int(i)
#         if sum % 2 == 0:
#             res.add(num)
#     return res
# nums = {12, 15, 23, 44, 111}
# print(filter_by_digit_sum(nums))

#20
# func = lambda d: [
#     k for k, v in sorted(
#         d.items(),
#         key=lambda x: (x[1], len(x[0]))
#     )
# ][:3]
# d = {"apple": 5, "kiwi": 2, "banana": 2, "pear": 7}
# print(func(d))

#21
# def count_leaf_values(d):
#     count = 0
#     for v in d.values():
#         if isinstance(v, dict):
#             count += count_leaf_values(v)
#         else:
#             count += 1
#     return count
# d = {
#     "a": 5,
#     "b": [1,2,3],
#     "c": {
#         "x": 10,
#         "y": {
#             "z": 7
#         }
#     }
# }
# print(count_leaf_values(d))

#22
# func = lambda a, b: {
#     x for x in a
#     if x not in b and x > sum(b)/len(b)
# }
# a = {1,2,3,4,5}
# b = {2,1,4}
# print(func(a,b))

#23
# def group_by_last_letter(words):
#     res = {}
#     for word in words:
#         last = word[-1]
#         if last not in res:
#             res[last] = []
#         if word not in res[last]:
#             res[last].append(word)
#     return res
# print(group_by_last_letter(["apple", "table", "tree", "coffee"]))

#24
# def union_of_filtered_sets(sets_list):
#     res = set()
#     for i in sets_list:
#         for num in i:
#             if num > 10 and num % 2 == 1:
#                 res.add(num)
#     return res
# sets_list = [{1, 11, 15}, {8, 13, 22}, {17, 4}]
# print(union_of_filtered_sets(sets_list))

#26
# def remove_eloements_with_common_digits(s):
#     res = {}
#     for i in s:
#         for j in str(i):
#             if j not in res:
#                 res[j] = 0
#             res[j] += 1
#     a = set()
#     for i in s:
#         ok = True
#         for j in str(i):
#             if res[j] > 1:
#                 ok = False
#                 break
#         if ok:
#             a.add(i)
#     return a
# s = {12, 34, 25}
# print(remove_eloements_with_common_digits(s))

#27
# nums = {2, 3, 4, 5, 6, 7, 8, 9, 10}
# is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))
# set_prime = set(filter(is_prime, nums))
# print(set_prime)

#28
# def sorted_unique_chars(strings):
#     unique_chars = set()
#     for string in strings:
#         for i in string:
#             if not i.isdigit() and i != " ":
#                 unique_chars.add(i)
#     return sorted(unique_chars)
# strings = ["hello", "world", "python3", "a b"]
# print(sorted_unique_chars(strings))

#29
# func = lambda x: sorted(
#     x.keys(),
#     key=lambda s: (x[s] % 10, s)
# )
# d = {"apple": 23, "banana": 12, "cherry": 32, "date": 42}
# print(func(d))

#30
# def partition_by_sum_parity(s):
#     a = {}
#     b = {}
#     for i in s:
#         c = 0
#         for j in str(i):
#             c += int(j)
#         if c % 2 == 0:
#             a[i] = i
#         else:
#             b[i] = i
#     return a, b
# s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
# print(partition_by_sum_parity(s))

#31
# func = lambda s: {
#     k: v
#     for k, v in s.items()
#     if len(v) == len(set(v)) and all(len(x) > 3 for x in v)
# }
# d = {
#     "a": ["apple", "pear", "pear"],
#     "b": ["tree", "book"],
#     "c": ["sun", "moon"]
# }
# print(func(d))

#32
# def pairwise_intersections(sets_list):
#     res = []
#     if len(sets_list) < 2:
#         return []
#     for i in range(len(sets_list)-1):
#         a = sets_list[i] & sets_list[i+1]
#         res.append(a)
#     return res
# sets_list = [{1,2,3}, {2,3,4}, {3,4,5}]
# print(pairwise_intersections(sets_list))

#33
# func = lambda s: {
#     k: v
#     for k, v in s.items()
#     if sum(v)/len(v) > sum(x for v in s.values() for x in v)/sum(len(v) for v in s.values())
# }
# s = {
#   "a": [1,2],
#   "b": [10,20],
#   "c": [5,5]
# }
# print(func(s))

#34
# def top_k_smallest_unique(nums, k):
#     a = set(nums)
#     sorted_list = sorted(a)
#     res = set()
#     lim = min(k, len(sorted_list))
#     for i in range(lim):
#         res.add(sorted_list[i])
#     return res
# print(top_k_smallest_unique([1,2,3,4,5,6,7,8,9], 3))

#35
# func = lambda s: {
#     k: v
#     for k, v in s.items()
#     if v % 3 != 0 and len(k) % 2 == 1
# }
# s = {"asd":11, "ed":32, "asdee": 12}
# print(func(s))

#36
# def all_subsets_of_size_k(s, k):
#     lst = list(s)
#     res = []
#     def a(b, c):
#         if len(c) == k:
#             res.append(set(c))
#             return
#         for i in range(b, len(lst)):
#             a(i+1, c + [lst[i]])
#     a(0, [])
#     return res
# print(all_subsets_of_size_k([1, 2, 3, 4, 5], 3))

#37
# import math
# func = lambda s: {
#     k: math.factorial(v) if v < 6 else v
#     for k, v in s.items()
# }
# s = {"a": 4, "b": 5, "c": 6, "d": 7}
# print(func(s))

#38
# def multi_symmetric_difference(sets_list):
#     if not sets_list:
#         return set()
#     res = sets_list[0]
#     for i in range(1, len(sets_list)):
#         res = res ^ sets_list[i]
#     return res
# sets_list = [{1,2,3},{2,5,6},{6,8,9}]
# print(multi_symmetric_difference(sets_list))

#39
# vowels = "aeuio"
# func = lambda s: sorted(
#     s.keys(),
#     key = lambda k: (
#         sum(1 for ch in k if ch in vowels),
#         -s[k]
#     )
# )
# d = {
#     "apple": 5,
#     "sky": 10,
#     "orange": 3,
#     "pear": 7
# }
# print(func(d))

#40
# def analyze_dict_keys(d):
#     res = set()
#     for key in d.keys():
#         if not isinstance(key, str):
#             continue
#         if any(ch.isdigit() for ch in key):
#             continue
#         for ch in key:
#             if ch.isalpha():
#                 res.add(ch)
#     return res
# d = {"hello": 1, "world123": 2, 45: "test", "hi there!": 3}
# print(analyze_dict_keys(d))

#Большая комплексная задача
# def analyze_orders(orders):
#     a = []
#     all_vowels = set()
#     for order in orders:
#         customer = order["customer"]
#         if any(ch.isdigit() for ch in customer):
#             continue
#         order["customer"] = customer.title()
#         processed = []
#         for item in order["items"]:
#             price = item["price"]
#             quantity = item["quantity"]
#             if price <= 0:
#                 continue
#             if price > 100 and quantity > 1:
#                 price = price * quantity
#             if quantity % 2 != 0:
#                 rounded = round(price)
#                 b = sum(int(d) for d in str(abs(rounded)))
#                 price += b
#             processed.append({"name": item["name"], "price": price, "quantity": quantity})
#     order["processed_items"] = processed
#     a.append(order)
#     c = " ".join(order["notes"])
#     d = "".join(
#         ch if ch.isalpha() or ch.isspace() else ""
#         for ch in c
#     )
#     words = d.lower().split()
#     filtered = [word for word in words if len(word) >= 4 and word != word[::-1]]
#     unique = set(filtered)
#     vowels = "aeiou"
#     for word in unique:
#         for ch in word:
#             if ch in vowels:
#                 all_vowels.add(ch)
#     unprod = set()
#     for order in a:
#         for item in order["processed_items"]:
#             unprod.add(item["name"])
#         order["total"] = sum(item["price"] for item in order["processed_items"])
#     orders_sorted = sorted(
#         a,
#         key = lambda s: (-s["total"], s["order_id"])
#     )
#     orders_by_item_count = {}
#     for order in a:
#         count = len(order["processed_items"])
#         if count not in orders_by_item_count:
#             orders_by_item_count[count] = []
#         orders_by_item_count[count].append(order["order_id"])
#     return {
#         "orders": a,
#         "all_vowels": all_vowels,
#         "unprod": unprod,
#         "orders_by_total": [o["order_id"] for o in orders_sorted],
#         "orders_by_item_count": orders_by_item_count
#     }
# orders = [
#     {
#       "order_id": "A123",
#       "customer": "john_doe42",
#       "items": [{"name": "Laptop", "price": 999.99, "quantity": 1},
#                 {"name": "Mouse2", "price": 25, "quantity": 2}],
#       "notes": ["Deliver ASAP", "fragile package", "handle with care"]
#     },
#     {
#       "order_id": "B456",
#       "customer": "alice",
#       "items": [{"name": "Keyboard", "price": 120, "quantity": 2}],
#       "notes": ["urgent delivery", "check packaging"]
#     }
# ]
# print(analyze_orders(orders))
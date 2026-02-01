#1
# def linear_search(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1
# print(linear_search([4, 9, 1, 7, 3, 5], 7))

#2
# def binary(nums, target):
#     first = 0
#     last = len(nums) - 1
#     while first <= last:
#         mid = (first + last) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             first = mid + 1
#         else:
#             last = mid - 1
# print(binary([2, 5, 8, 12, 16, 23, 38, 56], 23))

#3
# def linear(nums):
#     max = nums[0]
#     for num in nums:
#         if max < num:
#             max = num
#     return max
# print(linear([12, 99, 234, 7, 88, 42]))

#4
# def binary(nums, target):
#     first = 0
#     last = len(nums) - 1
#     while first <= last:
#         mid = (first + last) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             first = mid + 1
#         else:
#             last = mid - 1
#     return first
# print(binary([1, 4, 6, 9, 15], 8))

#5
# def linear(names, target):
#     for i in range(len(names)):
#         if names[i] == target:
#             return True
#     return False
# print(linear(["Alice", "Bob", "Charlie", "Diana", "Eva"], "Charlie"))

#6
# def binary(words, target):
#     first = 0
#     last = len(words) - 1
#     while first <= last:
#         mid = (first + last) // 2
#         if words[mid] == target:
#             return True
#         elif words[mid] < target:
#             first = mid + 1
#         else:
#             last = mid - 1
#     return False
# print(binary(["apple", "banana", "carrot", "grape", "orange", "peach"], "orange"))

#7
# def binary(users, target):
#     first = 0
#     last = len(users) - 1
#     while first <= last:
#         mid = (first + last) // 2
#         if users[mid]["id"] == target:
#             return users[mid]["name"]
#         if users[mid]["id"] < target:
#             first = mid + 1
#         else:
#             last = mid - 1
#     return None
# print(binary( [
#
# {"id": 101, "name": "Alex"},
#
# {"id": 215, "name": "Max"},
#
# {"id": 340, "name": "Anna"},
#
# {"id": 540, "name": "Tim"}
#
# ], 340))

#8
# def binary(nums, target):
#     first = 0
#     last = len(nums) - 1
#     while first <= last:
#         mid = (first + last) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             first = mid + 1
#         else:
#             last = mid - 1
#     if abs(nums[first] - target) < abs(nums[last] - target):
#         return nums[first]
#     else:
#         return nums[last]
# print(binary([2, 5, 9, 14, 20], 7))

#9
# def linear(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return True
#     return False
# def binary(nums, target):
#     first = 0
#     last = len(nums) - 1
#     while first <= last:
#         mid = (first + last) // 2
#         if nums[mid] == target:
#             return True
#         elif nums[mid] < target:
#             first = mid + 1
#         else:
#             last = mid - 1
#     return False
# def adaptive(nums, target):
#     if nums == sorted(nums):
#         return binary(nums, target)
#     else:
#         return linear(nums, target)
# print(adaptive([1, 3, 8, 12, 20], 12))
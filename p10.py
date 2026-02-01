#1
def a(nums):
    if nums == sorted(nums):
        return "YES"
    return "NO"
print(a([1, 7, 9]))

#2
def b(nums):
    max = sorted(nums)[-1]
    for num in range(len(nums) - 1, -1, -1):
        if nums[num] == max:
            return max, num
print(b([1,2,1,2,1]))

#3
def c(nums):
    count = [0] * 9
    i = 0
    while i < len(nums):
        x = nums[i]
        if x == 0:
            break
        count[x-1] += 1
        i += 1
    return count
print(c([4,9,3,4,2,4,9,4,3,8,0]))

#4
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
total = 0
for d, p in zip(dist, price):
    total += d*p
print(total)

#5
def d(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == 0:
                print(i, j)
                return
d([1,2,3,-2,-4])

#6
s = int(input())
sizes = list(map(int, input().split()))
sizes.sort()
count = 0
used = 0
for size in sizes:
    if used + size <= s:
        used += size
        count += 1
    else:
        break
print(count)

#7
c = int(input())
sizes = list(map(int, input().split()))
sizes.sort()
count = 0
a = c - 3
for size in sizes:
    if size >= a + 3:
        count += 1
        a = size
print(count)
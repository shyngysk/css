#1
# sq = [i**2 for i in range(1, 20) if i % 2 == 0]
# print(sq)

#2
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# res = [(lambda x: x[0]*x[1]*x[2])(x) for x in matrix]
# print(res)

#3
# words = ["кот", "машина", "ананас", "дом"]
# res = [i for i in words if len(i)>4 and "а" not in i]
# print(res)

#4
# numbers = [1,2,3,4,5]
# a = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
# print(a)

#5
# matrix = [[1,2], [3,4], [5,6]]
# res = [x for i in matrix for x in i]
# print(res)

#6
# res = ["Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else x for x in range(1,20)]
# print(res)
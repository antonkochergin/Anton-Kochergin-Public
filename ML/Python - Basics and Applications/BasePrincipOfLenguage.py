# ans = 0
# RepObjects = []
# for obj in objects:
#     if obj not in RepObjects:
#         RepObjects.append(obj)
#         ans += 1
#
# print(ans)

# def function_name(argument1 , argument2):
#     return argument1 + argument2
# print(id(function_name(2,8)))
# x = function_name(2,8)
# print(id(x))
# y = (function_name(8 , 2))
# print(id(y))

# def list_sum (lst):
#     result = 0
#     for element in lst:
#         result += element
#     return result
#
# def sum(a,b):
#     return a + b
#
# y = sum(14,29)
# z = list_sum([1,2,3])
# print(y)
# print(z)


#
# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
#
# y больше или равно x
# y делится нацело на 5

# def closest_mod_5(x):
#     for y in range(x,x**2):
#         if (y % 5 == 0):
#             return y
#     return "I don't know :("
# x = int(input())
# print(closest_mod_5(x))

# def printab(a, b, **kwargs):
#     print("positional argument a ", a)
#     print("positional argument b ", b)
#     print("additional arguments:")
#     for key in kwargs:
#         print(key, kwargs[key])
#
# printab(10, 20, с=30, d=40, jimmi=123)


# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
#

def c(n , k):
    if (k == 0) or (k == n): return 1
    if (k == 1): return n
    if (n < k ): return 0
    if (k>1):
        return c(n-1 , k) + c(n-1,k-1)

arg1,arg2 = map(int , input().split())
print(c(arg1,arg2))
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

def list_sum (lst):
    result = 0
    for element in lst:
        result += element
    return result

def sum(a,b):
    return a + b

y = sum(14,29)
z = list_sum([1,2,3])
print(y)
print(z)
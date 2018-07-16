x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}

z = {**x, **y}

print(z)
#
# data = dict(a=1, b=2, c=3)
#
# data.update(dict(a=10))
#
# print(data)
#
# data.update({'c': 3, 'd': 4})
#
# print(data)
#
# print('e' in data)
#
# l = [1, 2, 5]
# k = [3, 4, 6]
#
#
# def merge(a, b):
#
#     i = 0
#     j = 0
#
#     result = []
#
#     while True:
#
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1
#
#         if i >= len(a):
#             result.extend(b[j:])
#             return result
#
#         if j >= len(b):
#             result.extend(a[i:])
#             return result
#
#
# print(merge(l, k))

# 461_HammingDistance.py

def convert_bin(k):
    con = []
    while k > 0:
        # print('k: ', k)
        # print('before % calculation: ', con)
        con = [k % 2] + con
        # print('after % calculation: ', con)
        k //= 2
    return con
print(convert_bin(5))

def hammingDistance(x, y):
    bin_x = convert_bin(x)
    bin_y = convert_bin(y)
    cnt = 0
    if len(bin_x) > len(bin_y):
        len_diff = len(bin_x) - len(bin_y)
        i = 0 
        while i < len_diff:
            bin_y = [0] + bin_y
            i += 1
    if len(bin_x) < len(bin_y):
        len_diff = len(bin_y) - len(bin_x)
        i = 0 
        while i < len_diff:
            bin_x = [0] + bin_x
            i += 1
    for a, b in zip(bin_x, bin_y):
        if a != b:
            cnt += 1
    return cnt
print(hammingDistance(156,72))


# Fastest solution found in Discussion
# def hammingDistance(x, y):
#     print('x = ', x)
#     print('y = ', y)
#     x = x ^ y 
#     print('x: ', x)
#     y = 0
#     print('y: ', y)
#     while x:
#         y += 1
#         print('y -- ', y)
#         x = x & (x-1)
#         print('x -- ', x)
#     return y 
# print(hammingDistance(4,2))


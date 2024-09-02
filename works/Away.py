import PlainToolsB as pt

print(pt.pnumber(1/3, 10/33, 100/333, 1000/3333, dcm=16))
# import re
# import decimal
# import math

# def numperiod(num):
#     def RS(x, y): return round(x, y - max(repr(x)[
#         repr(x).find('.') + 1:].rstrip('0').count(
#         '0') // 4, repr(x)[repr(x).find(
#             '.') + 1:].rstrip('9').count('9') // 4))

#     def RT(x): return max(4, 16 - math.ceil(math.log(
#         x, 128 if x < 1e-15 else
#         64 if x < 1e-12 else
#         32 if x < 1e-9 else
#         16 if x < 1e-6 else
#         8 if x < 1e-3 else
#         4)))
    
    
#     num = RS(num, RT(abs(num)))

#     num = format(decimal.Context(prec=32).create_decimal(
#         repr(num)), 'f')
    
#     while re.compile(
#             r'^-?\d+\.\d*?[1-9](0{5,})([1-9]{1,2})$').search(num):
#         num = num[:-1]
        
#     snum, sdcm = str(math.floor(float(num))), repr(round(
#         abs(float(num) - math.floor(float(num))), len(
#         num.split('.')[1])))
    
#     rnum = num[::-1]  # Reverse the string representation of the number
#     fprd = None
#     for i in range(1, len(rnum) // 3 + 1):
#         period = rnum[:i]
#         if period * 3 in rnum:
#             fprd = period[::-1]
            
#     return float(snum + sdcm)

# x = 10/33
# print(x)
# print(numperiod(x))  # Output: '123'

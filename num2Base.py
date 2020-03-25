# -*-coding: utf-8-*-
# 将十进制整数转换成任意进制的字符串(使用递归）

def num2base(num, base):
    digits = '0123456789ABCDEF'
    if num // base == 0:
        return digits[num % base]
    else:
        return num2base(num // base, base) + digits[num % base]

print(num2base(15,16))

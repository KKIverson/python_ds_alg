# 使用递归实现汉诺塔（2^n -1 步)
def hanno(a, b, c, n):
    if n == 1:
        print(f'{a} --> {c}')
    else:
        hanno(a, c, b, n - 1)
        print(f'{a} --> {c}')
        hanno(b, a, c, n - 1)


hanno('A', 'B', 'C', 3)

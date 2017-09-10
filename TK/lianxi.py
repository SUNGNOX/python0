def is_odd(n):
    return n % 2 != 0
print(list(filter(is_odd, [1, 2, 3, 4, 5])))
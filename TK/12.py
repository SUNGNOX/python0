def built(x, y):
    return lambda: x*x + y*y

print(built(1, 2)())
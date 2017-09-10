def triangles():
    L = [1]
    yield L
    L.append(1)
    yield L
    n = 1


    while True:
        L1 = reduce(lambda x, y: x + y, L)
        L[0] = 1
        L[1:n] = L1
        L.append(1)
        n = n + 1
        yield L

g = triangles()
next(g)


def exp(a, n):
    p = 1
    for _ in range(1, n + 1): #  _  means it is unused but it also can use as a normal variable
        p = p * a
        #print(_)
    return p


print(exp(2,4))
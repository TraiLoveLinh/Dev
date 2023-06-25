def gcd(a, b):
    while a != b:
        if a > b:   
            a = a - b
        else:
            b = b - a
    return a

def gcd_res(a, b):
    if b == 0: 
        return a
    else:
        return(b, gcd_res(b, a % b))

print(gcd(16, 4))
print(gcd_res(16, 4))
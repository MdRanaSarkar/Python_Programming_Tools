def multiplypow(a, b):
    return a << b


def divpow2(a, b):
    return a >> b


# taking test case
t = int(input())
while t:
    v, p = map(int, input().split())
    print("Multipow2 value: ", multiplypow(v, p))
    print("divpow2 value: ", divpow2(v, p))

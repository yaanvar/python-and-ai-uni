def f(x):
    res = x
    res += res
    res += res
    res += res
    res2 = x - res
    res = res - res2
    return res

print(f(1))
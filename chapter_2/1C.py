def summation(*args):
    a = lambda x: -x * 2 if x < 0 else x
    b=list(map(a,list(args)))
    mass=[i/max(b) for i in b]
    return mass
print(summation(-1,3,4,-25,5))

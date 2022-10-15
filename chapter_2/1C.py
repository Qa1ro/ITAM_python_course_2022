a=lambda x: -x*2 if x<0 else x
def summation(*args):
    x=list(map(a,list(args)))
    mass=[i/max(x) for i in x]
    return mass


print(summation(-1,3,4,-25,5))
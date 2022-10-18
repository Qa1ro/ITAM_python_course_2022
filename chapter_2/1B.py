x=list(map(int,input().split()))
def summation(x):
    minimum=min(x)
    maximum=max(x)
    sum=0
    k=0
    while minimum<=maximum:
        k+=minimum
        minimum+=1
    return k
print(summation(x))

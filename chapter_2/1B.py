x=list(map(int,input().split()))
start=min(x)
end=max(x)
def summation(start,end):
    k=0
    while start!=end:
        k+=start
        start+=1
    return k+end
print(summation(start,end))
x=int(input())
def abob(x):
    k=1
    kaynter=0
    while x>=0:
        x-=k
        k+=1
        kaynter+=1
    return kaynter-1
print(abob(x))
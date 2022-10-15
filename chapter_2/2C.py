def convert(a,b):
    str1=""
    while a>0:
        str1+=str(a%b)
        a=a//b
    return str1[::-1]
print(convert(12,2))
a=input()
def greetings(a):
    b,c=a.split()
    return "Доброго времени суток, {},'Человек',{} ".format(b,c)
print(greetings(a))

dict_={}
def aye(dict1,dict2):
    mass=[i for i in dict1.keys()]
    mass1=[i for i in dict2.keys()]
    for i,v in dict1.items():
        for j,k in dict2.items():
            if i==j and v==k:
                dict_[i]="equal"
            elif i==j and v!=k:
                dict_[i]="changed"
            elif j not in mass:
                dict_[j]="added"
            elif i not in mass1:
                dict_[i]="deleted"
    return dict_
print(aye({"a":"b", "b":"a",  "c": "a"},{"a":"b", "b":"a"}))

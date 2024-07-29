'''students={}
students={"Alice":25,"Bob":27,"Clarie":17,"Dan":21,"Emma":22}
students["Dan"]#21
students["Fred"]=25
students["Fred"]#25
students["Alice"]=26
students["Alice"]#26
del students["Fred"]#will delete fred along with value
print(students)
students["Fred"]#couldnt find
students.keys()#give all keys
a=list(students.keys())
print(a)
students.values()#give all values but in dict
b=list(students.values())
print(b)#give in list
students.keys()[0]#error
students[0]#error'''
'''students={
    "Alice":["ID0001",26,"A"],
    "Bob":["ID002",27,"B"],
    "Clarie":["ID003",17,"c"],
    "Dan":["ID004",21,"D"],
    "Emma":["ID005",22,"E"]
}
print(students["Clarie"])
print(students["Clarie"][0])
print(students["Dan"][1:])'''
students={
    "Alice":{"id":"ID0001","age":26,"grade":"A"},
    "Bob":{"id":"ID0002","age":27,"grade":"B"},
    "Clarie":{"id":"ID0003","age":17,"grade":"c"},
    "Dan":{"id":"ID0004","age":21,"grade":"D"},
    "Emma":{"id":"ID0005","age":22,"grade":"F"}
}
print(students["Dan"]["age"])
print(students["Emma"]["id","grade"],students[ "Emma"]["grade"])



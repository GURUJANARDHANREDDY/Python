'''print(1,2,3,4,5)# 1 2 3 4 5
numbers=[1,2,3,4,5]
print(numbers)#[1,2,3,4,5]
print(*numbers)#unpacking=>1 2 3 4 5=>we take each item initerable data types each item will be one arguments
print("abc")#abc
print(*"abc")#a b c
def add(x,y):
    return x+y
add(10,10)'''
'''def add(*numbers):
    total=0
    for number in numbers:
        total+=number
    print(total)
add(1,2,3,4,5,6,7,8,9,10)'''
'''def about(name,age,likes):
    sentence="Meet {}! They are {} years old and they like {}".format(name,age,likes)
    print(sentence)
dictionary={"name":"ziyad","age":23,"likes":"python"}
about(**dictionary)'''#one star-arguments and two stars for keyword arguments
def foo(**kwargs):
    for key,value in kwargs.items():
        print("{} : {}".format(key,value))
foo(huda="female",ziyad="male",john="male")




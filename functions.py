#function is block of organised and reusable code that perform action and give result.

'''def add(x,y):
    return x+y
answer=add(5,10)
print(answer)'''
'''def add(x,y):
    print(x+y)
add(10,5)'''
#return and print are not same
#print shows result on screen but not store in variable name.
'''word="pen"
print(word[::-1])
'''
'''def rev(text):
    return text[::-1]
a=rev("pen")
b=rev([1,2,3,4])
print(a)
print(b)'''
#variable scope-> two types-> global(seen anywhere in program ->loops ,if not ) local (seen in local)
#python function create local
#we cannot change global variables inside the function automaticallly,but can use along as we change
#local variable when function completed
'''a=100#global scope
def f1():
    print(a)
def f2():
    print(a)
f1()
f2()'''
'''def f1():
    a=100#local variable
    print(a)
def f2():
    a=100#local variable is used when we have some many function we cannot define so variable name
    print(a)
f1()
f2()'''
'''a=250#global variable
def f1():
    a=50#local variable
    print(a)
def f2():
    a=100#local variable is used when we have some many function we cannot define so variable name
    print(a)
f1()#50
f2()#100
print(a)#250'''
'''a=250#global variable
def f1():
    b=a+10
    print(a)
def f2():
    a=100#local variable is used when we have some many function we cannot define so variable name
    print(a)
f1()#260
f2()#100
print(a)#250'''
'''#change global variable
a=250
def f1():
    global a
    a=100
    print(a)
def f2():
    a=50#local
    print(a)
f1()#100
f2()#50
print(a)#100'''
#for lists -no need to use global keyword to change
'''a=[1,2,3]
def f1():
    a[0]=5
    print(a)
def f2():
    a=50
    print(a)
f1()#[5,2,3]
f2()#50
print(a)#[5,2,3]'''
#keywords arguments and default parameters
'''def about(name,age,likes):#paramenters
    sentence="Meet {}! They are {} years old and they like {}".format(name,age,likes)
    print(sentence)
about("jack",23,"python")#arguments
about(age=23,name="jack",likes="python")#key arguments
def about(name,age,likes):#paramenters
    sentence="Meet {}! They are {} years old and they like {}".format(name,age,likes)
    print(sentence)
about("jack",23)'''#arguments=>error because 1 required position missing
'''def about(name,age,likes="python"):
    sentence="Meet {}! They are {} years old and they like {}".format(name,age,likes)
    print(sentence)
about("jack",23)#argument'''
'''def about(name="jACK",age=23,likes="python"):#paramenters=> default parameter at last always and we have many default parameters
    sentence="Meet {}! They are {} years old and they like {}".format(name,age,likes)
    print(sentence)
about("jack",21,"football")#arguments'''
def multiply(x,y):
    return x*y
answer=multiply(5,10)
print(answer)




  
#add,remove,present or not
'''l=[1,5,2,6,5,9]
2 in l #True
10 in l#False'''
'''l=[1,2,3,4,5]
del l[[0]]
l #[2,3,4,5]
example=["a","b","c","a","b"]
example.remove("a")
example ##["b","c","a","b"]
del example[3]#["a","b","c","b"]'''
'''known_users=["Alice","Bob","Clarie","Dan","Emma","Fred","Georgie","Harry"]
print(len(known_users))
while True:
    print("Hi! My name is John")
    name=input("What is your Name: ").strip().capitalize() #String are case sensitive we use captialize for getting first letter Captial-so it is recognised even small letter so given
    if name in known_users:
        print("Hello {}!".format(name)) 
        remove=input("would you like to be removed from the system(Y/n)?:").lower()
        if remove == "y":
            print(known_users.remove(name))
        elif remove == "n":
            print("no problem i didn't want to leave any way")
            
        
    else:
        print("Hmm I don't think i have met you yet {} ".format(name))
        add_me=input("would you like to be added to the system(y/n)?: ").lower()
        if add_me == "y":
           print(known_users.append(name))
        elif add_me == "n":
            print("No worries ,see you around")'''
known_users = ["Alice", "Bob", "Clarie", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

while True:
    print("Hi! My name is John")
    name = input("What is your Name: ").strip().capitalize()
    
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (Y/n)?: ").lower()
        if remove == "y":
            known_users.remove(name)
            print("You have been removed from the system.")
        elif remove == "n":
            print("No problem, you will remain in the system.")
            
    else:
        print("Hmm, I don't think I have met you yet, {}.".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").lower()
        if add_me == "y":
            known_users.append(name)
            print("You have been added to the system.")
        elif add_me == "n":
            print("No worries, see you around")




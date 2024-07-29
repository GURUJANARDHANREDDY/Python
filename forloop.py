'''for i in range(1,11):
    print(i)'''#print 1 to 10
'''for letter in "abcd":
    print(letter)'''
'''for i in range(1,11,2):
    print(i)#in step of 2'''
'''vowels=0
consonants=0
for letter in "Hello":
    if letter.lower() in"aeiou":
        vowels+=1
    elif letter=="":
        pass
    else:
        consonants+=1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))'''
'''vowels=0
consonants=0
for letter in "djdnwejnvjnjsnsjnjcfwrjnnxdjcfnwjorereroeoorkfekvorifm":
    if letter.lower() in"aeiou":
        vowels+=1
    elif letter=="":
        pass
    else:
        consonants+=1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))'''
'''students={
    "male":["jana","bhas","reddy","frank"],
    "female":["mad","lushi","sahi","tria"]
}
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
'''
#list compreshions
'''even=[x for x in range(1,101)if x%2==0]
print(even)'''
'''odd=[x for x in range(1,101)if x%2!=0]
print(odd)'''

words= ["the","quick","reddy","lazy","dog"]
answer=[[w.upper(),w.lower(),len(w)]for w in words]
print(answer)

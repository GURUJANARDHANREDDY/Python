word="supercalifragilisticexpialidocious"
word[0]
word[2]
#for morethan one letter slicng 
#syntax variablename[start:end:step]
word[0:5:1]#super
word[0:5:2]#spr
word[5:9:1]
word[5:]#califragilisticexpialidocious
word[5::2]#two steps
word[:7]#supercal
word[::-1]#reverse the string
word[-2]#u
word[-5]#c
word.index("cali")#5
word.index("fragi")#9
word[word.index("cali"):word.index("fragi")]#cali
word[word.index("fragilistic"):word.index("exp")]#fragalistic
word[word.index("fragilistic"):word.index("e")]#""
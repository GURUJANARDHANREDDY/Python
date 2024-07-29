'''A=[5,12,72,55,89]
A=A+[1]
A#[5,12,72,55,89,1]
A=A+["BCD"]
A#[5,12,72,55,89,1,'BCD']
A=A+list("BCD")
A#[5,12,72,55,89,1,'BCD','B','C','D']
A=A+list[123]
A#type error: int object not iterable
A=A+[1,2,3]
A#[5,12,72,55,89,1,'BCD','B','C','D',1,2,3]
A=A+list(str(123))
A#[5,12,72,55,89,1,'BCD','B','C','D',1,2,3,'1','2','3']
A=[5,12,72,55,89,1]
A#[5,12,72,55,89,1]
A=A+[[5,6,7,8]]
A#[5,12,72,55,89,1,5,6,7,8,[5,6,7,8]]
A.append([10,11,12,13])#[5,12,72,55,89,1,5,6,7,8,[5,6,7,8],[10,11,12,13]]'''
'''A=[5,12,72,55,89,1]
A=A.append(10)
print(A)
type(A)#none type'''
'''A=[5,12,72,55,89,1]
print(type(A.append(10))'''
'''A=[5,12,72,55,89,1]
A.insert(2,100)
print(A)
A.insert(2,[10,20,30])
print(A)
#lists are mutable it can be changed'''
'''A=[1,2,3]
A.remove(2)
print(A)#[1,2]
A=A.remove(2)
print(type(A))'''
list=[1,2,3,4,5,6,7]
list[2]=8
print(list)#[1,2,8,4,5,6,7]




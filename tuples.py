#tuples are immutable cannot be changed
tuple= 1,2,3,"A","B","C"
type(tuple)#tuple
tuple= (1,2,3,"A","B","C")#same
tuple[0:3]#(1,2,3)
#we cannot change elements in tuples
tuple[2]=100#tuple object does not support in assignment
A=[1,2,3]
A=tuple(A)
A#(1,2,3)
(A,B,C)=1,2,3
print(A)#1
print(B)#2
print(C)#3
D,E,F=[1,2,3]
print(D)#1
print(E)#2
print(F)#3
G,H,I="789"
print(G)#'7'
print(H)#'8'
print(I)#'9'
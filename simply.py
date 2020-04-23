from array import *

val = array('i',[1,2,3,4,5])
print(val)
arr = int(input("Enter the number to be serached "))
j=0
for val in range(len(val)):
    if arr==val:
     print(j)

j+=1
print("index no is "j)
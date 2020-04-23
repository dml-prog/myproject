num = int(input("enter "))

a=0
for i in range(1,num+1):
     for n in range(2,i):
        if i%n == 0:
            break

     else:
        print(i)
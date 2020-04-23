#checking string letter is > 5

def count(j):
    for i in range(5):
        num = str(input("Enter the name "))
        val = len(num)
        if val>5:
            j+=1

    return j

j =0
x = count(j)
print(x)
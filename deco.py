def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
def main():
    div1 = smart_div(div)
    div1(2,4)


if __name__=="__main__" :
     main()

#doubt

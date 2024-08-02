x=input("x=? >> ")
print(x)
try:
    x=int(x)
    if x>0:
        if(x%10==0):
            print("Last digit equal to 0")
        else:
            if x%10==1:
                print("Last digit equal to 1")
            else:
                print("none")
    else:
        if x==-1:
            print("Bye")
        else:
            print("Invalid Number")

except:
    print("Invalid Input")
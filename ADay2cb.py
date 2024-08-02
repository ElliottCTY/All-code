good=[]
num1=int(input("input number >> "))
if(num1>=0 and num1!=1):
    finalNum1=num1
    good.append(num1)
num2=int(input("input number >> "))
if(num2>=0 and num2!=1):
    finalNum2=num2
    good.append(num2)
num3=int(input("input number >> "))
if(num3>=0 and num3!=1):
    finalNum3=num3
    good.append(num3)
num4=int(input("input number >> "))
if(num4>=0 and num4%2!=1):
    finalNum4=num4
    good.append(num4)
num5=int(input("input number >> "))
if(num5>=0 and num5%2!=1):
    finalNum5=num5
    good.append(num5)
print(good)
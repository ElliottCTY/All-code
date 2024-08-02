weight=input("enter weight >> ")
des=input("enter destination >> ")
print(weight, des)
try:
    weight=int(weight)
    if des=="I":
        if weight<=1:
            cost=weight*0.01
        elif weight<=2:
            cost=weight*0.013
        elif weight<=4:
            cost=weight*0.015
        else:
            cost=weight*0.02
        print("shipping cost:",cost)
    else:
        if weight<=1:
            cost=10
        elif weight<=2:
            cost=20
        elif weight<=4:
            cost=50
        else:
            cost=60
        print("shipping cost:",cost)
except:
    print("Invalid Input")
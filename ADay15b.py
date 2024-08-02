Givenlist=[4,'MOO',7,'COW',11,'MOOSE',36,2.3,53.0,22.1,34,44]
print('\n')

def wash_int(part1,part2):
    for value in part1:
        try:
            if value==int(value):
                part2.append(value)
            elif value==float(value):
                part2.append(value)
            else:
                print("error")
        except:
            pass

def wash_non_int(part1):
    non_int=[]
    for value in part1:
        try:
            if value==int(value):
                pass
            elif value==float(value):
                pass
        except:
            non_int.append(value)
    print(f'the {len(non_int)} non-integers in the list are {non_int}')

def Maximum(what):
    num=[]
    wash_int(what,num)
    current=num[0]
    for a in range(0,len(num)):
        if num[a]>current:
            current=num[a]
        elif num[a]<=current:
            current=current
    print(f'{current} is the max/highest number')

def Minimum(thing):
    num=[]
    wash_int(thing,num)
    current=num[0]
    for a in range(0,len(num)):
        if num[a]<current:
            current=num[a]
        elif num[a]>=current:
            current=current
    print(f'{current} is the minimum/lowest number')

def Total(s):
    num=[]
    wash_int(s,num)
    current=0
    for i in range(0,len(num)):
        current+=num[i]
    print(f'{current} is the sum of all the numbers')

def Even(e):
    num=[]
    even=[]
    wash_int(e,num)
    for a in range(0,len(num)):
        if num[a]%2==0:
            even.append(num[a])
        elif num[a]%2!=0:
            pass
    print(f'the even numbers are {even}')



Maximum(Givenlist)
Minimum(Givenlist)
Total(Givenlist)
wash_non_int(Givenlist)
Even(Givenlist)

print('\n')
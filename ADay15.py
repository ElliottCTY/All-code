#2x2 matrix
#get inputs for matrix
#select addition or subtraction
def wash_int(thing,other):
    while True:
        try:
            value=input(f"number for row {thing+1} column {other+1} >> ")
            value=int(value)
            return value
        except:
            print("not a valid input")

def pretty(mat):
    for line in mat:
        for num in range(0,len(line)):
            print(line[num],end=' ')


part1=[["-","-"],
       ["-","-"]]
part2=[["-","-"],
       ["-","-"]]
part3=[["-","-"],
       ["-","-"]]


for a in range(0,2):
    for b in range(0,2):
        part1[a][b]=wash_int(a,b)
pretty(part1)
print("---------------")

for d in range(0,2):
    for e in range(0,2):
        part2[d][e]=wash_int(d,e)
pretty(part2)
print("---------------")


while True:
    choice=input("addition or subtraction >> ")
    if choice=="addition":
        for g in range(0,2):
            for h in range(0,2):
                part3[g][h]=part1[g][h]+part2[g][h]
        pretty(part3)
        print("---------------")
        break
    elif choice=="subtraction":
        for g in range(0,2):
            for h in range(0,2):
                part3[g][h]=part1[g][h]-part2[g][h]
        pretty(part3)
        print("---------------")
        break
    else:
        print("not an option")
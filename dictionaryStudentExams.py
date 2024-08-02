dict={"Charlie":{"grade1":94, "grade2":96, "grade3":0, "grade4":91}, "Sam":{"grade1":100, "grade2":98, "grade3":87, "grade4":97}, "Blair":{"grade1":89, "grade2":0, "grade3":89, "grade4":77}, "Karen":{"grade1":82, "grade2":92, "grade3":81, "grade4":0}, "Sarah":{"grade1":70, "grade2":30, "grade3":80, "grade4":92}}

choice=input("\ntype average, \ngrade, \nstudent amount, \npass, \nor add \n>> ")
if choice=="grade":
    y=input("student name >> ")
    print("\ngrade1\ngrade2\ngrade3\ngrade4\n")
    x=input("which grade do you want >> ")
    print(dict[y][x])
elif choice=="average":
    y=input("student name >> ")
    average=(dict[y]["grade1"]+dict[y]["grade2"]+dict[y]["grade3"]+dict[y]["grade4"])/4
    print(average)
elif choice=="student amount":
    print(len(dict))
elif choice=="pass":
    y=input("student name >> ")
    average=(dict[y]["grade1"]+dict[y]["grade2"]+dict[y]["grade3"]+dict[y]["grade4"])/4
    if average>=50:
        print("passed")
    elif average<50:
        print("failed")
elif choice=="add":
    name=input("what is the new student's name? >> ")
    g1=input("what is grade1? >> ")
    g2=input("what is grade2? >> ")
    g3=input("what is grade3? >> ")
    g4=input("what is grade4? >> ")
    dict[name]={"grade1":g1, "grade2":g2, "grade3":g3, "grade":g4}
    print(dict)
else:
        print("Sorry you input was invalid")

   
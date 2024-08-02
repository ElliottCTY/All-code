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

x=input('what number for x >> ')
y=input('what number for y >> ')
wash_int(x,None)
wash_int(y,None)

class calculator:
    def __init__(self):
        self.x=x
        self.y=y

    def add(self):
        return self.x+self.y
    
    def sub(self):
        return self.x-self.y
    
    def Mult(self):
        return self.x*self.y

    def Div(self):
        return self.x/self.y
            

calculator(x,y).add
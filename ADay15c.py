class brawler:
    def __init__(self,health,name,dps,super):
        self.health=health
        self.name=name
        self.dps=dps
        self.super=super
        self.XPos=None
        self.YPos=None

    def Move(self,Intended_XPos,Intended_Ypos):
        self.XPos=Intended_XPos
        self.YPos=Intended_Ypos
        print(f'{self.name} moved to {self.XPos},{self.YPos}')

    def damageTaken(self,TakenDamage):
        self.health=self.health-TakenDamage
        if self.health<=0:
            self.died
    
    def died(self):
        print(f'{self.name} has died \n')
        self.health=100
        self.Move(0,0,True)
    def regen(self,regenAmount):
        self.health+=regenAmount
player1=brawler(None,100,"thing",10,"gun")


class human:
    def __init__(self,age,name,hight,weight):
        self.age=age
        self.name=name
        self.hight=hight
        self.weight=weight
    
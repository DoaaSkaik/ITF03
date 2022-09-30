
class Vehicie :
    speed = 0
    has_wheels = False
    wheels_number = 0
    def setspeed_up (self,speed):
        self.speed=speed+5
    def getspeed_up(self):
        return self.speed
    def speed_down (self,speed):
        if speed==0:
            return
        self.speed=speed-5
    def stop (self) :
        self.speed=0
class Car (Vehicie):
    def __init__(self):
        self.has_wheels=True
        self.wheels_number=4
    def setspeed_up(self, speed):
        self.speed = speed + 10
    def getspeed_up(self):
        return self.speed
class Ship (Vehicie):
    def __init__(self):
        self.has_wheels=False
        self.wheels_number=0
    def setspeed_up(self,speed):
        self.speed=speed+20
    def getspeed_up(self):
        return self.speed
vehicie1=Vehicie()
vehicie1.setspeed_up(0)
print("\t\t\t\t\t\t\t\t\t\tthe normal speed in vehicie = " ,vehicie1.getspeed_up())
print("\t\t\t\t\t\t\t\t-----------------------------------------------")
car1=Car()
ship1=Ship()
print("\t\t\t\t\t\t\t\t\t\t","Car" ,"\t\t\t", "ship" )
print ("Has wheels ?","\t\t\t\t\t\t\t" ,car1.has_wheels,"\t\t\t",ship1.has_wheels)
print("the number of wheels ?" ,"\t\t\t\t\t",car1.wheels_number,"\t\t\t\t",ship1.wheels_number)
print ("the speed when stop ?" ,"\t\t\t\t\t",car1.speed,"\t\t\t\t",ship1.speed)
car1.setspeed_up(0)
ship1.setspeed_up(0)
print ("the speed when run ?" ,"\t\t\t\t\t",car1.getspeed_up(),"\t\t\t",ship1.getspeed_up())


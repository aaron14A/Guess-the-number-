class Car(object):

    def __init__(self , name , company , color , speedLimit):
        self.name = name
        self.company = company
        self.color = color 
        self.speedLimit = speedLimit
    
    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("accelaration")

    def changeGear(self , gearType):
        print("change Gear" + gearType)

audi = Car("The Tiger" , "Audi" , "Black" , 120 )
print(audi.color)
print(audi.start())


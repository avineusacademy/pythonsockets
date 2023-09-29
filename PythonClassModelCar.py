## Sample to understand python class

class vehicle:

    #initializer/ instance attributes
    def __init__(self, color, model, wheels):
        self.color = color
        self.model = model
        self.wheels = wheels
    
    #Function to show description
    def showVehicleDetails(self):
        print('This vehicle is of model : ', self.model, 'Color :', self.color, 'wheels', self.wheels)
       
    #Function to change the model
    def changeModel(self, model):
        self.model = model

    #function to change the color
    def changeColor(self, color):
        self.color = color
    
    #function to change number of wheels
    def changewheels(self, wheels):
        self.wheels = wheels

print('*********************************')
print('View details before changing \n')
print('********************************')

car = vehicle('white','SUV', 4)
jeep = vehicle('black','TUV', 4)
bike = vehicle('grey','Scooty', 2)
bus = vehicle('brown', 'Private',4)

##To view the details of vehicles
car.showVehicleDetails()
jeep.showVehicleDetails()
bike.showVehicleDetails()
bus.showVehicleDetails()

#To change color, model, wheels
car.changeColor('red')
jeep.changeModel('XUV')
bike.changewheels(3)
bus.changeColor('Yellow')

print('********************************')
print('View details after changing \n')
print('********************************')
##To view the details of vehicles
car.showVehicleDetails()
jeep.showVehicleDetails()
bike.showVehicleDetails()
bus.showVehicleDetails()


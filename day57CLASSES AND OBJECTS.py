#CLASSES AND OBJECTS(oops)

class person:
    name="aditya"
    occupation="persuaing goodness"
    networth=100000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
#self means the object on which the function is being called
#like a=person() and b=person() is called which prints the changed variables answers

a=person()
print(a.name,':',a.occupation)  

#but suppose u didint like the name or change the name 

a.name="virat"
a.occupation="cricketer"
print(a.name,':',a.occupation)

a.info()

b=person()
b.name="nitika"
b.occupation="HR"
b.info()
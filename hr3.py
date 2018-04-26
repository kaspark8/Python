import random

posx = ['left', 'center', 'right']
posy = ['top', 'middle', 'bottom']
rooms = ['living', 'kitchen', 'sauna', 'master bedroom', 'kids bedroom', 'bedroom', 'quest room']

class objFurniture:
    objCount = 0
    width = random.randint(0, 300)
    height = random.randint(0, 300)
    depth = random.randint(0, 300)
    color = "%06x" % random.randint(0, 0xFFFFFF)

    def __init__(self, width=width, height=height, depth=depth, color=color):
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color
        objFurniture.objCount += 1
        print("----")
    
    def myStats(self):
        print(f"My height is {self.height} cm, width {self.width} cm, depth {self.depth} cm and my color is #{self.color}.")

class objPosition:
    positionx = random.choice(posx)
    positiony = random.choice(posy)
    room = random.choice(rooms)

    def __init__(self, positionx=positionx, positiony=positiony, room=room):
        self.positionx = positionx
        self.positiony = positiony
        self.room = room
    
    def whereTheHellAmI(self):
        print(f"I am hiding in the {self.room}.")
    
class objSofa(objFurniture, objPosition):
    def __init__(self, name=None):
        self.name = name
    
    def whoAmI(self):
        print(f"My name is {self.name}.")

class objBed(objFurniture, objPosition):
    def __init__(self, name=None):
        self.name = name
    
    def whoAmI(self):
        print(f"My name is {self.name}.")

Sofa = objBed(name="Bedroom1")
Sofa.whoAmI()
Sofa.myStats()
Sofa.whereTheHellAmI()

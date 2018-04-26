import random

#room is 2D 
posx = ['left', 'center', 'right']
posy = ['top', 'middle', 'bottom']
rooms = ['living', 'kitchen', 'sauna', 'master bedroom', 'kids bedroom', 'bedroom', 'quest room']

class objSettings:
    objCount = 0
    width = random.randint(0, 300)
    height = random.randint(0, 300)
    depth = random.randint(0, 300)
    color = "%06x" % random.randint(0, 0xFFFFFF)

    def __init__(self, width=width, height=height, depth=depth, color=color, item=None, type=None):
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color
        objFurniture.objCount += 1
    
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


class objFurniture(objSettings, objPosition):
    def __init__(self, name=None, item=None, type=None):
        self.name = name
        self.item = item
        self.type = type
    
    def whoAmI(self):
        print(f"My name is {self.name} and I am {self.item} my type is {self.type}.")
    
    def moveMe(self, room, positionx, positiony):
        self.room = room
        self.positionx = positionx
        self.positiony = positiony
        print(f"My postition changed, now I am in {self.room} {self.positionx} {self.positiony}.")


Sofa = objFurniture(name="Master Bed", item="Bed", type="King Size")
Sofa.whoAmI()
Sofa.myStats()
Sofa.whereTheHellAmI()
Sofa.moveMe("bedroom", "middle", "right")

Table = objFurniture(name="Kitchen table", item="table", type="modern")
Table.whoAmI()
Table.myStats()
Table.whereTheHellAmI()
Table.moveMe("kitchen", "top", "center")

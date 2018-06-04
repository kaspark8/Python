import uuid

class objDrawAndPlaceMe:
    def __init__(self, name="Unknown", objwh=(0,0), room="living", description="Coming soon...", objtype="table", color="#FFF"):
        self.name = name
        self.objwh = objwh #width, height
        self.room = room
        self.description = description
        self.objtype = objtype
        self.color = color
        self.xyCoordinates = None

    def giveMeGUID(self):
        self.guid = uuid.uuid4().hex
        print("Object ID: " + self.guid)
  
    def positionObj(self):
        while True:
            askxyCoordinates = list(map(int, input("Insert object coordinates x:y, thanks!").split(":")))
            self.xyCoordinates = [askxyCoordinates[0], askxyCoordinates[0]+self.objwh[0], askxyCoordinates[1], askxyCoordinates[1]+self.objwh[1]]

            def isThereRoom(self):
                if xyCoordinatesList:
                    for xyc in xyCoordinatesList:
                        if (((xyc[0]<=self.xyCoordinates[0]<=xyc[1]) or (xyc[0]<=self.xyCoordinates[1]<=xyc[1])) and ((xyc[2]<=self.xyCoordinates[2]<=xyc[3]) or (xyc[2]<=self.xyCoordinates[3]<=xyc[3]))):
                            return True
                    return False
                else:
                    return False

            if isThereRoom(self):
                print("Value collides with existing one, insert new one.")
            else:
                xyCoordinatesList.append(self.xyCoordinates)
                drawMe(self)
                break


    def exportToAPI(self):
        pass

    def __str__(self):
        return "{}, type: {}, room: {}.".format(self.name, self.objtype, self.room)

def drawMe(obj):
    print("Drawing object: " + str(obj))

#list of object coordinates
xyCoordinatesList = []

#list of stuff to draw
objToDraw = [
    objDrawAndPlaceMe (name="Big Stool", objwh=(2,11), room="kitchen", description="Dam big stool.", objtype="stool", color="#FF0000"),
    objDrawAndPlaceMe (name="Big Table", objwh=(4,2), room="living", description="Dam big table.", objtype="table", color="#F2F2F2"),
    objDrawAndPlaceMe (name="Big Couch", objwh=(5,8), room="living", description="Dam big couch.", objtype="couch", color="#000000"),
    objDrawAndPlaceMe (name="Small wifi route", objwh=(1,1), room="living", description="Kinda small wifi route.", objtype="electronic", color="#FFFFFF"),
]


for obj in objToDraw:
    obj.positionObj()
    obj.giveMeGUID()
    obj.exportToAPI()

  
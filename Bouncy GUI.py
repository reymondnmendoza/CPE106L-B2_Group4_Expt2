
from breezypythongui import EasyFrame
def computeDistance(height, index, bounces):
    pass

class BouncyGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Bouncy")
        self.addLabel(text = "Initial Height",row = 0, column = 0)
        self.heightField = self.addIntegerField(value = 0,row = 0,column = 1, width = 10)
        self.addLabel(text = "Index",row = 1, column = 0)
        self.indexField = self.addFloatField(value = 0,row = 1,column = 1, width = 10)
        self.addLabel(text = "Number of Bounces",row = 2, column = 0)
        self.bouncesField = self.addIntegerField(value = 0,row = 2,column = 1, width = 10)
        self.compuuteButton = self.addButton(text = "Compute",row = 3, column =0,columnspan =2,
        command = self.computeDistance)
        self.addLabel(text = "Distance",row = 4, column = 0)
        self.distanceField = self.addFloatField(value = 0,row = 4,column = 1, width = 10)
    def computeDistance(self):
        height=self.heightField.getNumber()
        index=self.indexField.getNumber()
        bounces=self.bouncesField.getNumber()
        distance=0
        for eachPass in range(bounces):
            distance+=height
            height *=index
            distance+=height
        self.distanceField.setNumber(distance)

def main():

 BouncyGUI().mainloop()
if __name__ == "__main__":
 main()

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
 def __init__(self):
     EasyFrame.__init__(self, title = "Tax Calculator")
     self.addLabel(text = "Gross income",row = 0, column = 0)
     self.incomeField = self.addFloatField(value = "0.0",row = 0,column = 1, width=20)
     self.addLabel(text = "Dependents",row = 1, column = 0)
     self.depField = self.addIntegerField(value = "0",row = 1,column = 1,width=10)
     self.computeButton = self.addButton(text = "Compute",row = 2, column =0,columnspan =2,
                                         command = self.computeTax)
     self.addLabel(text = "Total tax",row = 3, column = 0)
     self.taxField = self.addFloatField(value = "0.0",row = 3,column = 1,width=20,precision=2)
 def computeTax(self):
     income=self.incomeField.getNumber()
     numDependents=self.depField.getNumber()
     exemptionAmount=3000.0
     standardDeduction=10000.0
     tax=(income-standardDeduction-(numDependents*exemptionAmount))*0.2
     self.taxField.setNumber(tax)
def main():
    TaxCalculator().mainloop()
if __name__ == "__main__":
 main()
 
 
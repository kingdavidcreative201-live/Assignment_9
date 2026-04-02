from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Application window for the tax calculator.
    Uses terminal version formula with 20% tax rate."""
    
    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator", width=300, height=200)
        
        # Income
        self.addLabel(text="Gross Income", row=0, column=0)  # Changed label
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1, width=15)
        
        # Dependents
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value=0, row=1, column=1, width=15)
        
        # Button (row changed to 2)
        self.addButton(text="Compute", row=2, column=0,
                       columnspan=2, command=self.computeTax)
        
        # Output (row changed to 3)
        self.addLabel(text="Total Tax", row=3, column=0)  # Changed label
        self.taxField = self.addFloatField(value=0.0, row=3, column=1, 
                                           width=15, precision=2, state="readonly")
    
    def computeTax(self):
        # NEW FORMULA HERE
        TAX_RATE = 0.20
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0
        
        grossIncome = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        
        taxableIncome = (grossIncome - STANDARD_DEDUCTION - 
                        (DEPENDENT_DEDUCTION * numDependents))
        
        if taxableIncome < 0:
            taxableIncome = 0
        
        incomeTax = taxableIncome * TAX_RATE
        self.taxField.setNumber(incomeTax)

if __name__ == "__main__":
    TaxCalculator().mainloop()
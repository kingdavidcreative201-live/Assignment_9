"""
tax_calculator_gui.py
Assignment 9 - Task 1: Tax Calculator GUI
Converts a terminal-based tax calculator to a GUI application.
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """
    Application window for the tax calculator.
    Calculates tax based on: (income - dependents * exemption) * tax_rate
    Default tax rate: 15% (0.15)
    """
    
    def __init__(self):
        """Sets up the window and widgets using the 6-step template."""
        # Step 1 & 2: Import is done above, class inherits from EasyFrame
        
        # Step 3: Initialize the window with title
        EasyFrame.__init__(self, title="Tax Calculator", width=300, height=200)
        
        # Step 4 & 5: Instantiate and position window components
        
        # Label and field for the income
        self.addLabel(text="Income", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1, width=15)
        
        # Label and field for the number of dependents
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value=0, row=1, column=1, width=15)
        
        # Label and field for the exemption amount
        self.addLabel(text="Exemption amount", row=2, column=0)
        self.exeField = self.addFloatField(value=0.0, row=2, column=1, width=15)
        
        # The command button - spans both columns
        self.addButton(text="Compute", row=3, column=0,
                       columnspan=2, command=self.computeTax)
        
        # Label and field for the tax result
        self.addLabel(text="Total tax", row=4, column=0)
        self.taxField = self.addFloatField(value=0.0, row=4, column=1, 
                                           width=15, precision=2, state="readonly")
    
    # Step 6: Define event handler method for the button
    def computeTax(self):
        """
        Event handler for the Compute button.
        Obtains data from input fields, calculates tax, and displays result.
        Formula: tax = (income - numDependents * exemptionAmount) * 0.15
        """
        try:
            # Get values from input fields
            income = self.incomeField.getNumber()
            numDependents = self.depField.getNumber()
            exemptionAmount = self.exeField.getNumber()
            
            # Calculate tax (15% flat rate)
            tax = (income - numDependents * exemptionAmount) * 0.15
            
            # Ensure tax is not negative
            if tax < 0:
                tax = 0
            
            # Display result
            self.taxField.setNumber(tax)
            
        except ValueError:
            # Handle invalid input
            self.messageBox(title="Input Error", 
                          message="Please enter valid numbers in all fields.")

# Instantiate and pop up the window
if __name__ == "__main__":
    TaxCalculator().mainloop()
from breezypythongui import EasyFrame
import tkinter.filedialog

class FileDialogDemo(EasyFrame):
    """Demonstrates the use of a file dialog."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "File Dialog Demo")
        
        self.outputArea = self.addTextArea("", 
                                           row = 0, column = 0,
                                           width = 80, 
                                           height = 15)
        
        self.addButton(text = "Open", row = 1, column = 0, 
                       command = self.openFile)

    def openFile(self):
        """Pops up an open file dialog, and if a file is 
        selected, displays its text in the text area."""
        fList = [("Python files", "*.py"), ("Text files", "*.txt")]
        
        fileName = tkinter.filedialog.askopenfilename(parent = self,
                                                      filetypes = fList)
        
        if fileName != "":
            file = open(fileName, 'r')
            self.outputArea.setText(file.read())
            file.close()
            self.setTitle(fileName)

if __name__ == "__main__":
    FileDialogDemo().mainloop()
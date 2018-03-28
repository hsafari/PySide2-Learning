# This will create a blank window with an icon.

import sys # Needed to get command line arguements

from PySide2.QtWidgets import QApplication, QWidget
# QApplication is need for flow control of program and the main settings.
# QWidget class is the base class of all user interface objects.

from PySide2.QtGui import QIcon # Get the package to add an icon


class FirstWindow(QWidget): # Set QWidget as a class of the main window
    
    def __init__(self):
        super().__init__()
        
        self.blank() # Call the blank window
        
    def blank(self):
        
        self.setWindowTitle('Hello World') # Set title of window
        
        self.setWindowIcon(QIcon('file.png')) # Set the window icon and add it
        
        self.resize(300, 300) # Resize the window
        
        self.show() # Show the window
        
app = QApplication(sys.argv) # Allow the taking of command line arguements

first = FirstWindow() # Call the window
sys.exit(app.exec_()) # Ensure the execution stops correctly

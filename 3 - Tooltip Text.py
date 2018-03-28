# This will create a blank window with an icon.

import sys # Needed to get command line arguements

from PySide2.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
# QApplication is need for flow control of program and the main settings.
# QWidget class is the base class of all user interface objects.
# QToolTip to set the tooltip 
# QPushButton creates a pushable button

class FirstWindow(QWidget): # Set QWidget as a class of the main window
    
    def __init__(self):
        super().__init__()
        
        self.blank() # Call the blank window
        
    def blank(self):
        
        button = QPushButton('Hover Over Me!', self) # Create the button
        button.setToolTip('Hello World') # Set the text of the tooltip on the button
        button.resize(button.sizeHint()) # Resize the button to the suggested height
        
        
        
        self.resize(300, 300) # Resize the window
        self.show() # Show the window
        
app = QApplication(sys.argv) # Allow the taking of command line arguements

first = FirstWindow() # Call the window
sys.exit(app.exec_()) # Ensure the execution stops correctly

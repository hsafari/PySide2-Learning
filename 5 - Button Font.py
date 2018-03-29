# This will create a blank window with an icon.

import sys # Needed to get command line arguements

from PySide2.QtWidgets import QApplication, QWidget, QPushButton
# QApplication is need for flow control of program and the main settings.
# QWidget class is the base class of all user interface objects.
# QPushButton creates a pushable button

from PySide2.QtGui import QFont # Select between fonts

class FirstWindow(QWidget): # Set QWidget as a class of the main window
    
    def __init__(self):
        super().__init__()
        
        self.blank() # Call the blank window
        
    def blank(self):
        
        button = QPushButton('Press Me!', self) # Create the button
       
        button.setFont(QFont('SansSerif', 20)) # Apply font and font size to button
        
        button.clicked.connect(QApplication.instance().quit) # Cause the window to quit when button is clicked
        button.resize(button.sizeHint()) # Resize the button to the suggested height
        button.move(30, 0) # Move where the button is located
        # The first arguement is to the right
        # The second is downwards
        
        
        
        self.resize(300, 300) # Resize the window
        self.show() # Show the window
        
app = QApplication(sys.argv) # Allow the taking of command line arguements

first = FirstWindow() # Call the window
sys.exit(app.exec_()) # Ensure the execution stops correctly

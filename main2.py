# WEIGHT MANAGEMET APPLICATION MAIN

# Libraries and modules
import kivy # The Kivy framework
kivy.require('2.0.0') # Minimun version of the framework
from kivy.app import App # A parent class for the main window
from kivy.uix.gridlayout import GridLayout # A parent

# Initializations and class definitions 

# The GridLayout
class Glayout(GridLayout):

    # Functional parts ie methods
    def calculate_bmi(self): # Calculates Body Mass Index
        pass

    def calculate_fat(self): # Calculates Fat percentage
        pass

# Create the app 
class WieghtManagementApp(App):
    def build(self):
        return Glayout()

# Run the app
if __name__ == '__main__':
    # Create the App object
    wieghtManagementApp = WieghtManagementApp()

    # Run it continuously
    wieghtManagementApp.run()

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
        person_height = float(self.height_value.text)/100
        person_weight = float(self.weight_value.text)
        person_bmi = round(person_weight / person_height ** 2)
        self.bmi_value.text = str(person_bmi)
        


    def calculate_fat(self): # Calculates Fat percentage
        person_age = float(self.age_value.text)
        person_weight = float(self.weight_value.text)
        person_age = float(self.age_value.text)
        person_sex = float(self.sex_value.text)
        # TODO: person_fatpercentage
# Create the app 
class WeightManagementApp(App):
    def build(self):
        return Glayout()

# Run the app
if __name__ == '__main__':
    # Create the App object
    weightManagementApp = WeightManagementApp()

    # Run it continuously
    weightManagementApp.run()

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.calculate_diameter()
        self.area = self.calculate_area()
        self.circumference = self.calculate_circumference()

    def __str__(self):
        return f'Diameter: {self.diameter} \nCircumference: {self.circumference} \nArea: {self.area}'

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_circumference(self):
        return (self.radius * 2 * pi)
    
    def calculate_area(self):
        return pi * (self.radius ** 2)

    def grow(self):
        '''This function doubles the radius of the circle'''
        self.radius = self.radius * 2

    def get_radius(self):
        return self.radius
 
if __name__ == '__main__':
    # Validate radius input
    while True:
        radius = input('Please enter the radius of your circle \n> ')
        try:
            radius = float(radius)
        except ValueError:
                print('Invalid input. Please try again.')
        else:
            circle1 = Circle(radius)
            break
    # Print info        
    print(circle1)  
    # If user says yes, radius doubles and runs the methods again
    grow_choice = input('Would you like your circle to grow? (y/n) \n> ').lower()
    if grow_choice == 'y' or grow_choice.lower == 'yes':
        circle1.grow() 
        circle1 = Circle(circle1.radius)
        print(circle1)
    else:
        print('Thank you for participating! Goodbye!')
        
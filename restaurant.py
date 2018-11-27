"""A class to represent a restaurant."""

class Restaurant():
    """Describe a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10
    
    def describe_restaurant(self):
        """Describe the restaurant."""
        print("\nThis restaurant is called " + self.restaurant_name.title() + ".")
        print("This restaurant serves " + self.cuisine_type.title() + ".")
        print('This restaurant has served ' + str(self.number_served) + ' customers.')
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")
        
    def increment_number_served(self, number):
        self.number_served += number
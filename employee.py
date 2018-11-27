class Employee():

    def __init__(self, first_name, last_name, salary):
        """Initiate attributes to describe an employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def increment_salary(self, money=5000):
        self.salary += money
        
       

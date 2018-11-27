import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""
        
    def setUp(self):
        self.my_employee = Employee('john', 'doe', 40000)
    
    def test_increment_salary(self):
        """Test that increment_salary works."""
        self.my_employee.increment_salary()
        self.assertEqual(self.my_employee.salary, 45000)
        
    def test_custom_raise(self):
        """Test that increment_salary works with a custom ammount."""
        self.my_employee.increment_salary(1000)
        self.assertEqual(self.my_employee.salary, 41000)
        
       
unittest.main()
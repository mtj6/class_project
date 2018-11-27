import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""
    
    def test_city_country(self):
        """Do cities like Santiago, Chile work?"""
        formated_city = city_country('santiago', 'chile')
        self.assertEqual(formated_city, 'Santiago, Chile')
        
    def test_city_country_population(self):
        """Do cities like Santiago, Chile - population 500000 work?"""
        formated_city = city_country('santiago', 'chile', '500000')
        self.assertEqual(formated_city, 'Santiago, Chile - population 500000')
        
unittest.main()
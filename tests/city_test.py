import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):
    def setUp(self):
        self.country = Country("Scotland", 5, True, 1)
        self.city = City("Dundee", self.country, 5, True, 1)


    def test_city_has_name(self):
        self.assertEqual("Dundee", self.city.name)

    def test_city_has_country(self):
        self.assertEqual(1, self.city.country.id)

    def test_city_has_rating(self):
        self.assertEqual(5, self.city.rating)

    def test_city_has_visited(self):
        self.assertEqual(True, self.city.visited)

    def test_city_has_id(self):
        self.assertEqual(1, self.city.id)
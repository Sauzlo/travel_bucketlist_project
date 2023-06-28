import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Scotland", 5, True, 1)


    def test_country_has_name(self):
        self.assertEqual("Scotland", self.country.name)

    def test_country_has_rating(self):
        self.assertEqual(5, self.country.rating)

    def test_country_has_visited(self):
        self.assertEqual(True, self.country.visited)

    def test_country_has_id(self):
        self.assertEqual(1, self.country.id)
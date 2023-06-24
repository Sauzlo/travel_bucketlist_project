import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country1 = Country("Scotland", 5)
country_repository.save(country1)

city1 = City("Dundee", country1)
city_repository.save(city1)



pdb.set_trace()
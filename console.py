import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Scotland")
country_repository.save(country1)

country2 = Country("France")
country_repository.save(country2)

country3 = Country("Italy")
country_repository.save(country3)

city1 = City("Dundee", country1)
city_repository.save(city1)

city2 = City("Edinburgh", country1)
city_repository.save(city2)

city3 = City("Aberdeen", country1)
city_repository.save(city3)

city4 = City("Glasgow", country1)
city_repository.save(city4)

city5 = City("Paris", country2)
city_repository.save(city5)

select_country = country_repository.select(country1.id)
print(select_country.__dict__)

select_city = city_repository.select(city1.id)
print(select_city.__dict__)

select_all_countries = country_repository.select_all()
for country in select_all_countries:
    print(country.__dict__)

country1 = Country("United Kingdom")
country_repository.update(country1)

print(country1.__dict__)

city1 = City("London", country1)
city_repository.update(city1)

print(city1.__dict__)


pdb.set_trace()
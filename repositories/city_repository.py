from db.run_sql import run_sql
from models.city import City


def save(city):
    sql = "INSERT INTO cities (name, visited, country_id) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.visited, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['country_id'], row['visited'], row['id'])
        cities.append(city)
    
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        row = result[0]
        city = City(row['name'], row['country_id'], row['visited'], row['id'])

    return city


def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)
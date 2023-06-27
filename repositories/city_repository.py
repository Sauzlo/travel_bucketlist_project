from db.run_sql import run_sql
from models.city import City


def save(city):
    sql = "INSERT INTO cities (name, rating, visited, country_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [city.name, city.rating, city.visited, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['country_id'], row['rating'], row['visited'], row['id'])
        cities.append(city)
    
    return cities


def select_by_country(country_id):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country_id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['country_id'], row['rating'], row['visited'], row['id'])
        cities.append(city)

    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        row = result[0]
        city = City(row['name'], row['country_id'], row['rating'], row['visited'], row['id'])

    return city


def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql = "UPDATE cities SET (name, rating, country_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.rating, city.country.id, city.visited, city.id]
    run_sql(sql, values)
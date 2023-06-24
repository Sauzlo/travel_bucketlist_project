from db.run_sql import run_sql
from models.country import Country


def save(country):
    sql = "INSERT INTO countries (name, rating, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [country.name, country.rating, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['rating'], row['visited'], row['id'])
        countries.append(country)
    
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        row = result[0]
        country = Country(row['name'], row['rating'], row['visited'], row['id'])

    return country

def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, rating, visited) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.rating, country.visited, country.id]
    run_sql(sql, values)
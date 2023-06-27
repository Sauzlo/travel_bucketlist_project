from flask import Blueprint, request, redirect, render_template
from models.city import City
from models.country import Country
from repositories import city_repository, country_repository

from flask import Blueprint

cities_blueprint = Blueprint('cities', __name__)

@cities_blueprint.route('/cities/<id>')
def show(id):
    city = city_repository.select(id)
    country = country_repository.select(city.country)
    return render_template('/cities/show.html', city=city, country=country)


@cities_blueprint.route('/cities/new')
def new():
    countries = country_repository.select_all()
    return render_template('/cities/new.html', countries=countries)


@cities_blueprint.route('/cities', methods=['POST'])
def create():
    name = request.form["name"]
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    city = City(name, country)
    city_repository.save(city)
    return redirect(f'/countries/{country_id}')
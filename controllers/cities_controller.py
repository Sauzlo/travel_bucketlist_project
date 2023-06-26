from flask import Blueprint, request, redirect, render_template
from models.city import City
from repositories import city_repository, country_repository

from flask import Blueprint

cities_blueprint = Blueprint('cities', __name__)

@cities_blueprint.route('/cities/<id>')
def show(id):
    city = city_repository.select(id)
    country = country_repository.select(city.country)
    return render_template('/cities/show.html', city=city, country=country)
from flask import Blueprint, request, redirect, render_template
from models.country import Country
from repositories import country_repository, city_repository

from flask import Blueprint

countries_blueprint = Blueprint('countries', __name__)


@countries_blueprint.route('/countries')
def index():
    countries = country_repository.select_all()
    return render_template('/countries/index.html', countries=countries)


@countries_blueprint.route('/countries/new')
def new():
    return render_template('/countries/new.html')


@countries_blueprint.route('/countries', methods=['POST'])
def create():
    name = request.form["name"]
    country = Country(name)
    country_repository.save(country)
    return redirect('/countries')


@countries_blueprint.route('/countries/<id>')
def show(id):
    country = country_repository.select(id)
    cities = city_repository.select_by_country(id)
    return render_template('/countries/show.html', country=country, cities=cities)
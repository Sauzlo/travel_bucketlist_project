from flask import Blueprint, request, redirect, render_template
from models.country import Country
from repositories import country_repository

from flask import Blueprint

countries_blueprint = Blueprint('countries', __name__)


@countries_blueprint.route('/countries')
def index():
    countries = country_repository.select_all()
    return render_template('/countries/index.html', countries=countries)


@countries_blueprint.route('/countries/<id>')
def show(id):
    country = country_repository.select(id)
    return render_template('/countries/show.html', country=country)
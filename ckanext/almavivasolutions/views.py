from flask import Blueprint


almavivasolutions = Blueprint(
    "almavivasolutions", __name__)


def page():
    return "Hello, almavivasolutions!"


almavivasolutions.add_url_rule(
    "/almavivasolutions/page", view_func=page)


def get_blueprints():
    return [almavivasolutions]

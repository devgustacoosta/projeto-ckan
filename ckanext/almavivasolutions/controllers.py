import ckan.logic as logic
from flask import Blueprint, render_template, g

bp = Blueprint('almavivasolutions', __name__, url_prefix='/')

@bp.route('/about-us')
def sobre():
    return render_template('about-us.html')

@bp.route('/open-government')
def openGovernment():
    return render_template('open-government.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/user-guide')
def userGuide():
    return render_template('user-guide.html')

@bp.route('/metrics')
def metrics():
    return render_template('metrics.html')
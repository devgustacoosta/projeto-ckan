import ckan.logic as logic
from flask import Blueprint, render_template, g

bp = Blueprint('almavivasolutions', __name__, url_prefix='/')

@bp.route('/organization/data-gov-eua')
def dataGovEUA():
    return render_template('organization/data-eua.html', page={})

@bp.route('/organization/dados-abertos-goias')
def dadosGO():
    return render_template('organization/data-go.html', page={})

@bp.route('/organization/helsinki-region-infoshare')
def dadosGB():
    return render_template('organization/data-gb.html', page={})


# @bp.route('/open-government')
# def openGovernment():
#     return render_template('open-government.html')

# @bp.route('/contact')
# def contact():
#     return render_template('contact.html')

# @bp.route('/user-guide')
# def userGuide():
#     return render_template('user-guide.html')

# @bp.route('/metrics')
# def metrics():
#     return render_template('metrics.html')
from flask import Blueprint, render_template

bp = Blueprint('almavivasolutions', __name__, url_prefix='/')

@bp.route('/about-us')
def sobre():
    return render_template('/about-us.html')
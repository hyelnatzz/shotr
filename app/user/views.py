from . import user_bp
from flask import render_template


@user_bp.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template('user/dashboard.html')


@user_bp.route('/gstatistics/', methods=['GET', 'POST'])
def general_statistics():
    return 'Statistics page'


@user_bp.route('/ustatistics/<int:url_id>/')
def url_statistics(url_id):
    return f'Logout Endpoint {url_id}'

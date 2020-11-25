from . import auth_bp
from flask import render_template


@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('auth/signin.html')


@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    return render_template('auth/signup.html')

@auth_bp.route('/logout/')
def logout():
    return 'Logout Endpoint'
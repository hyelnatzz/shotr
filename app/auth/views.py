from . import auth_bp


@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    return "Login Page"


@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    return 'Sign up page'

@auth_bp.route('/logout/')
def logout():
    return 'Logout Endpoint'
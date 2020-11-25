from . import user_bp


@user_bp.route('/', methods=['GET', 'POST'])
def dashboard():
    return "User Dashboard Page"


@user_bp.route('/gstatistics/', methods=['GET', 'POST'])
def general_statistics():
    return 'Statistics page'


@user_bp.route('/ustatistics/<int:url_id>/')
def url_statistics(url_id):
    return f'Logout Endpoint {url_id}'

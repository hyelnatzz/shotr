from . import urls_bp


@urls_bp.route('/<string>/')
def redirect(string):
    return string


@urls_bp.route('/addurl/')
def addurl():
    return 'Add Url page '


@urls_bp.route('/delete/<int:url_id>/')
def deleteurl(url_id):
    return f'Delete Url Page {url_id}'


@urls_bp.route('/edit/<int:url_id>/')
def editurl(url_id):
    return f'edit URL Page {url_id}'

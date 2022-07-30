from flask.templating import render_template
from . import urls_bp
from flask import redirect, url_for, flash
from ..models import Urls, ShortUrl
from .. import db
from flask_login import login_required, current_user


@urls_bp.route('/<string>/')
def redirect_url(string):
    short_url = ShortUrl.query.filter_by(value = string).first()
    if short_url:
        short_url.url.visits = short_url.url.visits + 1
        db.session.commit()
        return render_template('redirect.html', url=short_url.url.url_address)
    if not current_user.is_anonymous:
        flash('URL does not exist, create one below.')
        return redirect( url_for('user_bp.dashboard'))
    flash('URL does not exist, Sign Up or Sign In to create one')
    return redirect(url_for('home_bp.index'))


@urls_bp.route('/addurl/', methods=['POST'])
def addurl():
    return 'Add Url page '


@urls_bp.route('/delete/<int:url_id>/')
@login_required
def deleteurl(url_id):
    url = Urls.query.filter_by(id = url_id).first()
    url.delete()
    flash('URL deleted')
    return redirect(url_for('user_bp.dashboard'))


@urls_bp.route('/edit/<int:url_id>/')
@login_required
def editurl(url_id):
    return f'edit URL Page {url_id}'

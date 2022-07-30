from flask.helpers import url_for
from werkzeug.utils import redirect
from . import user_bp
from ..forms import UrlAddForm
from ..models import Urls, ShortUrl
from ..utils import create_short
from flask import render_template, flash
from flask_login import login_required, current_user


@user_bp.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = UrlAddForm()
    links = Urls.query.filter_by(author_id = current_user.id).all()
    urls = sorted(links, key=lambda x: x.visits )
    urls.reverse()
    if form.validate_on_submit():
        url = Urls.query.filter_by(name=form.name.data.strip()).first(
        ) or Urls.query.filter_by(name=form.url.data.strip()).first()
        if not url:
            url = Urls()
            url.name = form.name.data.strip()
            url.url_address = form.url.data.strip()
            url.author = current_user
            url.save()
            short = ShortUrl()
            short.value = create_short()
            short.url = url
            short.save()
            flash('Url Added Successfully')
        else:
            flash('Url already Exist')
        return redirect(url_for('user_bp.dashboard'))

    return render_template('user/dashboard.html', form=form, links = links, urls = urls)


@user_bp.route('/gstatistics/', methods=['GET', 'POST'])
def general_statistics():
    return 'Statistics page'


@user_bp.route('/ustatistics/<int:url_id>/')
def url_statistics(url_id):
    return f'Logout Endpoint {url_id}'

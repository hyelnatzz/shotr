from flask import redirect, url_for
from . import auth_bp
from flask import render_template, flash
from ..forms import SignInForm, SignUpForm, UrlAddForm
from ..models import User
from flask_login import login_user, logout_user, login_required
from flask import request


@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data.strip().lower()).first()
        if user:
            if user.check_password(form.password.data.strip()):
                login_user(user, remember=form.remember_me)
                return redirect(request.args.get('next', url_for('user_bp.dashboard')))
            else:
                flash('Incorrect Username or password')
                return redirect( url_for('auth_bp.login'))
    return render_template('auth/signin.html', form=form)


@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data.strip().lower()
        user.username = form.username.data.strip().lower()
        user.set_password(form.password.data.strip())
        user.save()
        flash('Sign Up Successful')
        return redirect(url_for('auth_bp.login'))
    return render_template('auth/signup.html', form=form)

@auth_bp.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('User logged out')
    return redirect(url_for('auth_bp.login'))

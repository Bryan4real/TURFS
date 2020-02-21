from flask import render_template,request,redirect,url_for, abort
from . import main
from .. import db
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm, UpdateProfile
from ..models import Review, User
from flask_login import login_required, login_user,logout_user

@main.index('/')
def index():

    title = "TURFS"

    return render_template('index.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data   

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)                              
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..requests import get_quote
from flask_login import login_required,current_user
from ..models import Blog, User
from .forms import UpdateProfile
from .. import db,photos


@main.route('/')
def index():
  '''
  View root function that returns the index page and its data.
  '''
  title = "Blog App"

  return render_template('index.html', title = title)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
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

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/blogs')
@login_required
def blogs():
    '''
    View function that returns the page containing the blogs and its data.
    '''
    quote = get_quote()

    blogs = Blog.query.order_by(Blog.posted_on.desc())

    title='Blogs'

    return render_template('blogs.html', blogs = blogs, title= title, quote = quote)


    





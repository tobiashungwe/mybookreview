from re import template
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Review, User
from . import db


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home(): 
 reviews = Review.query.all()
 return render_template("home.html", user=current_user, reviews=reviews)


@views.route("/create-review", methods=['GET','POST'])
@login_required
def create_review(): 
    if request.method == "POST": 
        text = request.form.get('text')

        if not text:
            flash('Review cannot be empty', category='error')
        else:
            review = Review(text=text, reviewer=current_user.id)
            db.session.add(review)
            db.session.commit()
            flash('Review created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("create_review.html", user=current_user)

@views.route("/delete-review/<id>")
@login_required
def delete_review(id): 
    review = Review.query.filter_by(id=id).first()
    
    if not review:
        flash("Review does not exist", category='error')
    elif current_user.id != review.id:
        flash('You do not have the permission to delete this review!', category='error')
    else:
        db.session.delete(review)
        db.session.commit()
        flash('Review deleted', category='success')
    return redirect(url_for('views.home'))
    
@views.route("/reviews/<username>")
@login_required
def reviews(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))
    
    reviews = Review.query.filter_by(reviewer=user.id).all()
    return render_template("reviews.html", user=current_user, reviews=reviews, username=username)
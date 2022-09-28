from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Review, User, Comment
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
    
    reviews = user.reviews
    return render_template("reviews.html", user=current_user, reviews=reviews, username=username)

@views.route("/create-comment/<review_id>", methods=['POST'])
@login_required
def create_comment(review_id):
    text = request.form.get('text')
    
    if not text: 
        flash('Comment cannot be empty.', category='error')
    else:
        review = Review.query.filter_by(id = review_id)
        if review:
            comment = Comment(text=text, reviewer=current_user.id, review_id=review_id)
            db.session.add(comment)
            db.session.commit()
        else:
         flash('Review does not exist!', category='error')

    return redirect(url_for('views.home'))


@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id): 
    comment = Comment.query.filter_by(id=comment_id).first()
    
    if not comment:
        flash('Comment does not exist!', category='error')
    elif current_user.id != comment.reviewer and current_user.id != comment.review.reviewer:
        flash('You do not have the permission to delete this comment', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('views.home'))
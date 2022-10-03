import json
from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response
from flask_login import login_required, current_user
from Models.Comment import Comment
from Models.Like import Like
from Services.Books_select import get_dropdown_booklist
import Services.database_pymongo
from Models.Review import Review
from Models.User import User
from Utilities.Methods import display_error, success_response


mod = Blueprint("review_routes", __name__)

@mod.route("/")
@mod.route("/home")
@login_required
def home(): 
 reviews = Review.objects
 print(reviews)
 success_response(reviews.to_json())
 resp = make_response(render_template("home.html", user=current_user, reviews=reviews))
 resp.set_cookie("reviews", str(reviews))
 return resp


@mod.route("/create-review", methods=['GET','POST'])
@login_required
def create_review(): 
    book_list = get_dropdown_booklist()
    if request.method == "POST": 
        text = request.form.get('text')
        
        if not text:
            display_error('Review cannot be empty')
        else:
            review = Review(text=text, reviewer=current_user.id)
            review.save()
            flash('Review created!', category='success')
            
            resp = redirect(url_for('review_routes.home'), code=200, Response=success_response(review.to_json()))
        return resp
    
    return render_template("create_review.html",  dropdown=book_list.to_html(escape=False, index=False), user=current_user)

@mod.route("/delete-review/<id>")
@login_required
def delete_review(id): 
    review = Review.objects(id=id).first()
    
    if not review:
        display_error("Review does not exist")
    elif current_user.id != review.id:
        display_error("You do not have the permission to delete this review!")
    else:
        review.delete()
        flash('Review deleted', category='success')
    return redirect(url_for('review_routes.home'), code=200, Response=success_response(review.to_json()))
    
@mod.route("/reviews/<username>")
@login_required
def reviews(username):
    user = User.objects(name=username).first()

    if not user:
        display_error('You do not have the permission to edit this review')
        return redirect(url_for('review_routes.home'), code=200, Response=success_response(user.to_json()))
    
    reviews = Review.objects(reviewer=user.id)
    resp = make_response(render_template("reviews.html", user=current_user, reviews=reviews, username=username))
    resp.set_cookie("reviews", str(reviews))
    return resp

@mod.route("/create-comment/<review_id>", methods=['POST'])
@login_required
def create_comment(review_id):
    text = request.form.get('text')
    
    try:
        if not text: 
            display_error('Comment cannot be empty.')
        else:
            review = Review.objects(id = review_id).first()
            if review:
                comment = Comment(text=text, reviewer=current_user.id, review_id=review_id)   
                
                # Add to comments list and saved_end
                review.comments.append(comment)
                review.save()
            else:
                display_error("Review does not exist!")
                
        return redirect(url_for('review_routes.home'), code=200, Response=success_response(comment.to_json()))
    except:
        display_error('Something went wrong, reloading!')
    return redirect(url_for('review_routes.home', code=300 ))

@mod.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id): 
    comment = Comment.objects(id=comment_id).first()
    
    if not comment:
     display_error("Comment does not exist!")
    elif current_user.id != comment.reviewer and current_user.id != comment.review.reviewer:
     display_error("You do not have the permission to delete this comment!")
    else:
        comment.delete()

    return redirect(url_for('review_routes.home'), code=200, Response=success_response(comment.to_json()))

# @mod.route("/like-review/<review_id>", methods=['GET'])
# @login_required
# def like(review_id) -> None: 
    
    
#     review = Review.objects(id=review_id).first()
    
#     if not current_user and not review_id:
#         if not review:
#             display_error("Review does not exist")
#         if not review:
#             display_error("Please Sign in")
#     else: 
       
#         # Find current review
#         review = Review.objects.filter(id=review_id).first()

#         # Create a new like for current review
#         like = Like(reviewer=current_user.id, review_id=review_id)

#         #Check the like list for current user
#         review_potentially_liked = Review.objects.filter(id=review_id, reviewer=current_user.id).first()
        
        
#         try:
#             if not review_potentially_liked:
#                 # Add to like list and save if already liked
#                 review.likes.append(like)
#                 review.save()
#             else:
#                 #remove from like list if already liked
#                 review.likes.remove(like)
#                 review.save()
#         except:
#               display_error("Error: Can not like this review for you!")
                   
#     return redirect(url_for('review_routes.home'))
       
@mod.route("/like-review/<review_id>", methods=['GET'])
@login_required
def like(review_id): 
  
        reviews = Services.database_pymongo.ConnectPymongo.db.reviews
        reviewId = reviews.insert_one({"review_id": review_id}).inserted_id
        review = reviews.find_one(reviewId)
        likes = Services.database_pymongo.ConnectPymongo.db.likes
        like = likes.find_one(filter={"reviewer": current_user.id, "review_id": reviewId})

        if not review:
            flash('Review does not exist', category='error')
        elif like:
            likes.delete_one(like)
        else:
            like = Like(reviewer=current_user.id, review_id=review_id).to_json()
            likes.insert_one(like) 
        
        return redirect(url_for('review_routes.home'))
   
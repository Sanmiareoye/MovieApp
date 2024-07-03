from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import Movie, MyList
from flask_login import login_required, current_user
from .utils import fetch_movies, fetch_movies_by_id
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    search_text = 'far'
    if request.method=='POST':
        search_text = request.form.get('search-field')
        print(search_text)
    all_movies = []
    
    for page in range(1, 6):  # Fetch the first 5 pages
        movie_data = fetch_movies(search_text, page)
        if not movie_data:
            break
        all_movies.extend(movie_data)
    
    return render_template('home.html', movies=all_movies)

@views.route('/mylist', methods=['GET', 'POST'])
@login_required
def mylist():
    if request.method == 'POST':
        data = json.loads(request.data)
        movie_id = data.get('movieId')
        
        exsisting_movie = MyList.query.filter_by(imdbId=movie_id, user_id=current_user.id).all()
        if exsisting_movie:
            flash('Movie already listed!', category='error')
        else:
            movie = fetch_movies_by_id(movie_id)
            print('hello')
            print(movie)
            if movie:
                listmovie = MyList(imdbId=movie_id, user_id=current_user.id)
                db.session.add(listmovie)
                db.session.commit()
                flash('Movie added to Your List!', category='success')
    print('hello')
    
    user_list = MyList.query.filter_by(user_id=current_user.id).all()
    movies = [fetch_movies_by_id(item.imdbId) for item in user_list]
    
    return render_template('mylist.html', user=current_user, movies=movies)

@views.route('/delete-movie', methods=['POST'])
@login_required
def delete_movie():
    data = json.loads(request.data)
    movie_id = data.get('movieId')
    
    movie = MyList.query.filter_by(imdbId=movie_id, user_id=current_user.id).first()
    
    if movie:
        if movie.user_id == current_user.id:
            db.session.delete(movie)
            db.session.commit()
            flash('Movie Deleted!', category='success')
    return jsonify({})
    




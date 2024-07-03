import requests
from flask import current_app

def fetch_movies(search, page=1):
    api_key = current_app.config['OMDB_API_KEY']
    url = 'http://www.omdbapi.com/'
    params = {
        'apikey': api_key,
        's': search,       # Example: Search for movies with title 'Star Wars'
        'type': 'movie',   # Example: Specify type as 'movie'
        'page': page         # Example: Pagination, if applicable
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        movies_data = response.json().get('Search', [])
        return movies_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return []
    
def fetch_movies_by_id(id):
    api_key = current_app.config['OMDB_API_KEY']
    url = 'http://www.omdbapi.com/'
    params = {
        'apikey': api_key,
        'i': id,       # Example: Search for movies with title 'Star Wars'
        'type': 'movie',   # Example: Specify type as 'movie'       # Example: Pagination, if applicable
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        movies_data = response.json()
        return movies_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return []




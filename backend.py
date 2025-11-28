import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
movies_data = pd.read_csv("movies.csv")

selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

GENRE_WEIGHT = 3 

# Repeat the genres text to give it more importance in TF-IDF
genres_weighted = (movies_data['genres'] + ' ') * GENRE_WEIGHT

combined_features = (
    genres_weighted +
    movies_data['keywords'] + ' ' +
    movies_data['tagline'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['director']
)

# 4. Create TF-IDF vectors and similarity matrix
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)


def recommend_movies(movie_name: str, num_recommendations: int = 10):

    if not movie_name:
        return []

    list_of_all_titles = movies_data['title'].tolist()
    close_matches = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not close_matches:
        return []

    close_match = close_matches[0]

    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    # Get similarity scores for that movie
    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    # Sort movies based on similarity score 
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    # Prepare final recommendations
    recommendations = []
    i = 0
    for movie in sorted_similar_movies:
        index = movie[0]

        title_from_index = movies_data[movies_data.index == index]['title'].values[0]

        if title_from_index not in recommendations:
            recommendations.append(title_from_index)
            i += 1
            if i >= num_recommendations:
                break

    return recommendations

def get_all_titles():
    """Return a list of all movie titles."""
    return movies_data["title"].dropna().tolist()


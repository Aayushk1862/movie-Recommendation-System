import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=bf3df81db77708e8bf784dbc5ea48665&language=en-US'.format(
            movie_id))

    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)

        # will use this to fetch poster from API

    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Which Movie you saw last?',
    movies['title'].values)

if st.button('Show Recommendations'):
    recommended_movie_names = recommend(selected_movie_name)
    for i in recommended_movie_names:
        st.write(i)
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:28:13 2023

@author: harivars
"""

import streamlit as st
import pickle as pk
import requests

def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x:x[1])[1:7]
    movies_recommended = []
    movies_posters = []
    for i in distances:
        movie_id = movies.iloc[i[0]].movie_id
        movies_recommended.append(movies.iloc[i[0]].title)
        movies_posters.append(get_poster(movie_id))
    
    return movies_recommended,movies_posters

st.header('Movie Recommender System')
movies = pk.load(open('movies_list.pkl','rb'))
similarity = pk.load(open('similarities.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)
selected_id = movies[movies['title'] == selected_movie].movie_id.iloc[0]

if st.button('Show Recommendation'):
    movies_recommended,movies_posters = recommend_movies(selected_movie)
    st.write('Selected Movie - ', selected_movie)
    st.image(get_poster(selected_id), width=240)
    st.write('----------------------------------------------')
    st.subheader('Movie Recommendations')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(movies_recommended[0])
        st.image(movies_posters[0])
        st.write('-------------------')
    with col2:
        st.markdown(movies_recommended[1])
        st.image(movies_posters[1])
        st.write('-------------------')

    with col3:
        st.markdown(movies_recommended[2])
        st.image(movies_posters[2])
        st.write('-------------------')
    with col1:
        st.markdown(movies_recommended[3])
        st.image(movies_posters[3])
        st.write('-------------------')
    with col2:
        st.markdown(movies_recommended[4])
        st.image(movies_posters[4])
        st.write('-------------------')
    with col3:
        st.markdown(movies_recommended[5])
        st.image(movies_posters[5])
        st.write('-------------------')
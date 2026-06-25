import streamlit as st
import pickle
import requests


similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = movies_list['title'].values
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_distances = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movie_distances:
        movie_id = movies_list.iloc[i[0]]
        recommended_movies.append(movies_list.iloc[i[0]]['title'])
    return recommended_movies

st.title('Movie Recommender')


option = st.selectbox(
    'Select a Movie to watch similar kind of ',
    movies)

if st.button('Recommend'):
    recommended = recommend(option)
    for i in recommended:
        st.write(i)
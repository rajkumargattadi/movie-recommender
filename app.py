import pandas as pd
import streamlit as st
import pickle
import requests




def fetch_poster(movie_title):
    api_key='3fb6a8a8&y'
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    poster_url = data.get("Poster")
    if poster_url and poster_url != "N/A":
        return poster_url
    else:
        return "https://via.placeholder.com/500x750.png?text=No+Poster"




def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_five = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]

    for i in movies_five:

        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        poster_url = fetch_poster(title)

        recommended_movies_posters.append(poster_url)



    return recommended_movies,recommended_movies_posters


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)


similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_movie=st.selectbox(
    'select movie to get recommendation ',
    movies['title'].values
)


if st.button("Recommend"):
    names,posters=recommend(selected_movie)

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
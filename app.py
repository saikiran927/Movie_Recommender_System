import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url='https://api.themoviedb.org/3/movie/{}?api_key=dd8218b84b59390ae13ca0e5d0b1efc7&language=en-US'.format(movie_id)
    response=requests.get(url,verify=False)
    data=response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = similarity[index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:6]
    recommend_movie=[]
    recommend_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))

    return recommend_movie,recommend_poster

movies=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title(":red[Movie Recommender System]")


selected_movie=st.selectbox("Select movie from dropdown", movies['title'].values)
print("This is movie recomendor system")

# this is the streamlit code 
if st.button("Show Recommend"):
    movie_name,movie_poster=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(movie_poster[0])
        st.text(movie_name[0])
    with col2:
        st.image(movie_poster[1])
        st.text(movie_name[1])
    with col3:  
        st.image(movie_poster[2])
        st.text(movie_name[2])
    with col4:
        st.image(movie_poster[3])
        st.text(movie_name[3])
    with col5:
        st.image(movie_poster[4])
        st.text(movie_name[4])





import streamlit as st
import pickle 
import pandas as pd




def recommend(movie_title):
    if movie_title not in movies['title'].values:
        print(f"Movie '{movie_title}' not found in the dataset.")
        return

    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarty[movie_index]  # Assuming 'similarty' is calculated elsewhere
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    

    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies



movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarty = pickle.load(open('similarty.pkl','rb'))

st.title("Movie Recommdetion Syatem")
select_movie_name = st.selectbox(

'How would you like  to be contacted',
movies['title'].values
)
if st.button(' Show Recommend'):
    recommended=recommend(select_movie_name)
    recommended_movie_names = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        #st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        #st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        #st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        #st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        #st.image(recommended_movie_posters[4])






    
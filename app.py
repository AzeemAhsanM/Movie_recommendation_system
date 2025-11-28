import streamlit as st
from backend import recommend_movies

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Type a movie name and get similar movie suggestions.")

# ---- SEARCH FORM (Enter will submit this form) ----
with st.form(key="search_form"):
    movie_name = st.text_input("Enter a movie name:")
    submitted = st.form_submit_button("Recommend")  

# ---- HANDLE SUBMISSION ----
if submitted:
    if not movie_name.strip():
        st.warning("Please type a movie name first.")
    else:
        recommendations = recommend_movies(movie_name)

        if not recommendations:
            st.error("Sorry, I couldn't find that movie in the database.")
        else:
            st.subheader("Movies suggested for you:")
            for i, title in enumerate(recommendations, start=1):
                st.write(f"{i}. {title}")

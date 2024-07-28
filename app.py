import streamlit as st
from huggingface import generate_restaurant_name_and_items

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items']  # Already a list, no need to strip and split
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

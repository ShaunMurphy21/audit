import streamlit as st
st.title("Desk 5")

st.write(":red[DESK PICTURES BELOW]")


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Desk 5/desk51.jpg")
    st.image("./assets/Desk 5/desk53.jpg")


with col2:
    st.image("./assets/Desk 5/desk52.jpg")

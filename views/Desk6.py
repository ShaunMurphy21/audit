import streamlit as st
st.title("Desk 6")
st.write(":red[DESK PICTURES BELOW]")


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Desk6/desk61.jpg")
    st.image("./assets/Desk6/desk62.jpg")
    st.image("./assets/Desk6/desk64.jpg")


with col2:
    st.image("./assets/Desk6/desk63.jpg")
    st.image("./assets/Desk6/desk65.jpg")
import streamlit as st
st.title("Desk 7")
st.write(":red[DESK PICTURES BELOW]")


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Desk7/desk71.jpg")
    st.image("./assets/Desk7/desk72.jpg")



with col2:
    st.image("./assets/Desk7/desk73.jpg")
    st.image("./assets/Desk7/desk74.jpg")
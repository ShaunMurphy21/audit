import streamlit as st

st.title("IT")
st.write(":red[DESK PICTURES BELOW]")

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/IT Desk/it1.jpg")
    st.image("./assets/IT Desk/it2.jpg")





with col2:
    st.image("./assets/IT Desk/it3.jpg")
    st.image("./assets/IT Desk/it4.jpg")
import streamlit as st
st.title("CustomerService")


st.title("Customer Service Desk")
st.write(":red[DESK PICTURES BELOW]")


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/CS 225/cs1.jpg")
    st.image("./assets/CS 225/cs2.jpg")



with col2:
    st.image("./assets/CS 225/cs3.jpg")
    st.image("./assets/CS 225/cs4.jpg")
import streamlit as st

import streamlit as st
st.title("Nick")
st.write(":red[Pictures of desk below]")
@st.dialog("Nick Contact Information")
def show_contact_form():
    st.text("Email: nick.carey@highwaycare.com")
    st.text("Teams:  ncarey@highwaycare.com")
    st.text("Phone ext:  205")
if st.button("Contact Information"):
    show_contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Nick 205/nick1.jpg")
    st.image("./assets/Nick 205/nick2.jpg")


with col2:
    st.image("./assets/Nick 205/nick3.jpg")
    st.image("./assets/Nick 205/nick4.jpg")


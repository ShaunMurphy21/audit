import streamlit as st


st.title("Russe;")
st.write(":red[DESK PICTURES BELOW]")
@st.dialog("Glenn Contact Info")
def show_contact_form():
    st.text("Email: russell.how@highwaycare.com")
    st.text("Teams:  rhow@highwaycare.com")
    st.text("Phone ext:  212")
if st.button("Contact Information"):
    show_contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Russel 212/russel1.jpg")
    st.image("./assets/Russel 212/russel2.jpg")

with col2:
    st.image("./assets/Russel 212/russel3.jpg")
    st.image("./assets/Russel 212/russel4.jpg")
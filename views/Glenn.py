import streamlit as st

st.title("Glenn")
st.write(":red[DESK PICTURES BELOW]")
@st.dialog("Glenn Contact Info")
def show_contact_form():
    st.text("Email: glen.legrys@highwaycare.com")
    st.text("Teams:  glen.legrys@highwaycare.com")
    st.text("Phone ext:  NONE")
if st.button("Contact Information"):
    show_contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Glenn none/glenn1.jpg")

with col2:
    st.image("./assets/Glenn none/glenn2.jpg")
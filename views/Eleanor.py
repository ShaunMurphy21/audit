import streamlit as st

st.title("Eleanor")
st.write(":red[DESK PICTURES BELOW]")

@st.dialog("Eleanor Contact Information")
def show_contact_form():
    st.text("Email: eleanor.wood@highwaycare.com")
    st.text("Teams:  eleanor.wood@highwaycare.com")
    st.text("Phone ext:  215")
if st.button("Contact Information"):
    show_contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Eleanor 215/eleanor1.jpg")




with col2:
    st.image("./assets/Eleanor 215/eleanor2.jpg")

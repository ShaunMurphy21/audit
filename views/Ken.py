import streamlit as st
st.title("Ken")
st.write(":red[Please see desk pictures below]")


@st.dialog("Ken Contact Information")
def show_contact_form():
    st.text("Email: ken.hutchins@highwaycare.com")
    st.text("Teams:  khutchins@highwaycare.com")
    st.text("Phone ext:  220")
if st.button("Contact Information"):
    show_contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Ken 220/ken1.jpg")
    st.image("./assets/Ken 220/ken2.jpg")


with col2:
    st.image("./assets/Ken 220/ken3.jpg")
    st.image("./assets/Ken 220/ken4.jpg")
import streamlit as st




st.title("Annie")
st.title("Desk 7")
st.write(":red[DESK PICTURES BELOW]")

@st.dialog("Annie Contact Info")
def show_contact_form():
    st.text("Email: annie.boyd@highwaycare.onmicrosoft.com")
    st.text("Teams:  annie.boyd@highwaycare.com")
    st.text("Phone ext:  206")

if st.button("Contact Information"):
    show_contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Annie206/Annie1.jpg")
    st.image("./assets/Annie206/Annie2.jpg")



with col2:
    st.image("./assets/Annie206/Annie3.jpg")
    st.image("./assets/Annie206/Annie4.jpg")

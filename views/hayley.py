import streamlit as st
st.title("Hayley")
st.write(":red[Pictures of desk below]")
@st.dialog("Haley Contact Information")
def show_contact_form():
    st.text("Email: hayley.terrell@highwaycare.com")
    st.text("Teams:  hayley.terrell@highwaycare.com")
    st.text("Phone ext:  208")



if st.button("Contact Information"):
    show_contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/Hayley 208/hayley1.jpg")
with col2:
    st.image("./assets/Hayley 208/hayley2.jpg")
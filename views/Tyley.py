import streamlit as st

st.title("Tyley")
st.write(":red[DESK PICTURES BELOW]")
@st.dialog("Tyley Contact Info")
def show_contact_form():
    st.text("Email: tyley.boozer@highwaycare.com")
    st.text("Teams: tboozer@highwaycare.com")
    st.text("Phone ext:  218")
if st.button("Contact Information"):
    show_contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Tyley 218/PXL_20240918_163201814.jpg")


with col2:
    st.image("./assets/Tyley 218/PXL_20240918_163203688.jpg")

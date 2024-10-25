import streamlit as st

st.title("Susan")
st.write(":red[DESK PICTURES BELOW]")
@st.dialog("Susan Contact Info")
def show_contact_form():
    st.text("Email: susan.power@highwaycare.com")
    st.text("Teams:  spower@highwaycare.com")
    st.text("Phone ext:  217")
if st.button("Contact Information"):
    show_contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Susan 217/PXL_20240918_163300621.jpg")
    st.image("./assets/Susan 217/PXL_20240918_163303353.jpg")

with col2:
    st.image("./assets/Susan 217/PXL_20240918_163307843.jpg")
    st.image("./assets/Susan 217/PXL_20240918_163315845.jpg")
import streamlit as st

st.title("Spare Desk")
st.write(":red[DESK PICTURES BELOW]")
@st.dialog("Glenn Contact Info")
def show_contact_form():
    st.text("Email: N/A")
    st.text("Teams:  N/A")
    st.text("Phone ext:  216")
if st.button("Contact Information"):
    show_contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Spare 216/PXL_20240918_163340468.jpg")
    st.image("./assets/Spare 216/PXL_20240918_163343440.jpg")

with col2:
    st.image("./assets/Spare 216/PXL_20240918_163347222.jpg")
    st.image("./assets/Spare 216/PXL_20240918_163350132.jpg")

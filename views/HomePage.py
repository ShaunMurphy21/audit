import streamlit as st
@st.dialog("Inform of Desk Changes")
def show_contact_form():
    st.text_input("First Name")



col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/OIP (1).jfif")
with col2:
    st.image("./assets/ASL.PNG")
st.image("./assets/Whole Office/PXL_20240918_140545727.jpg",)


st.subheader("About HighwayCare", anchor=False)
st.write("""
         Highway Care is a leading provider of innovative road safety solutions and services, specializing in
         the supply and installation of barriers, traffic management systems, and vehicle restraint systems.
         With a focus on enhancing safety on highways and major roads, the company offers products and
         services designed to protect road users and workers. Highway Care combines cutting-edge
         technology with industry expertise to deliver reliable, high-quality solutions, contributing to safer
         road environments across the UK and beyond.
     """
)



st.subheader("Please Inform me if any changes need adding using the below button😊")
if st.button("📧Inform me of changes"):
    show_contact_form()



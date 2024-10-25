import streamlit as st

st.title("Mel")
st.write(":red[Pictures of desk below]")
@st.dialog("View Mel Contact Information")
def show_contact_form():
    st.text("Email: melanie.tragner@highwaycare.com")
    st.text("Teams: mtragner@highwaycare.com")
    st.text("Phone ext: 224")
if st.button("Contact Information"):
    show_contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Mel224/mel1.jpg")
    st.image("./assets/Mel224/mel2.jpg")
with col2:
    st.image("./assets/Mel224/mel3.jpg")
    st.image("./assets/Mel224/mel4.jpg")


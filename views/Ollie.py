import streamlit as st

st.title("Ollie")
st.write(":red[Pictures of desk below]")

@st.dialog("Ollie Contact Information")
def show_contact_form():
    st.text("Email: ollie.pulling@highwaycare.com")
    st.text("Teams:  opulling@highwaycare.com")
    st.text("Phone ext:  211")
if st.button("Contact Information"):
    show_contact_form()
col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Ollie 211/ollie1.jpg")
    st.image("./assets/Ollie 211/ollie2.jpg")


with col2:
    st.image("./assets/Ollie 211/ollie3.jpg")
    st.image("./assets/Ollie 211/ollie4.jpg")


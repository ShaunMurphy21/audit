import streamlit as st

@st.dialog("Jason Contact Information")
def show_contact_form():
    st.text("Email: jason.potter@highwaycare.com")
    st.text("Teams:  jpotter@highwaycare.com")
    st.text("Phone ext:  209")

st.title("Jason")
st.write(":red[Please see desk pictures below]")

if st.button("Contact Information"):
    show_contact_form()
col1, col2, col3,  = st.columns(3, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/Jason 209/jaon1.jpg")
    st.image("./assets/Jason 209/jason2.jpg")



with col2:
    st.image("./assets/Jason 209/jason3.jpg")
    st.image("./assets/Jason 209/jason4.jpg")



with col3:
    st.image("./assets/Jason 209/jason5.jpg")
    st.image("./assets/Jason 209/jason6.jpg")

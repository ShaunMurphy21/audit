import streamlit as st
st.title("David")
st.write(":red[Please see desk pictures below]")
@st.dialog("David Contact Info")
def show_contact_form():
    st.text("Email: david.armstrong@highwaycare.com")
    st.text("Teams:  darmstrong@highwaycare.com")
    st.text("Phone ext:  219")

if st.button("Contact Information"):
    show_contact_form()





col1, col2 = st.columns(2, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/David 219/david1.jpg")
    st.image("./assets/David 219/david2.jpg")


with col2:
    st.image("./assets/David 219/david3.jpg")
    st.image("./assets/David 219/david4.jpg")
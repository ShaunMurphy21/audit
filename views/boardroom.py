import streamlit as st
st.title("BoardRoom")
st.write(":red[PLEASE NOTE THIS INCLUDES PICTURES OF SERVER ALSO]")
col1, col2, col3, col4 = st.columns(4, gap="small", vertical_alignment="top")
with col1:
    st.image("./assets/BoardRoom1/b4.jpg")
    st.image("./assets/BoardRoom1/br1.jpg")
    st.image("./assets/BoardRoom1/br2.jpg")
    st.image("./assets/BoardRoom1/br3.jpg")
    st.image("./assets/BoardRoom1/br5.jpg")
    st.image("./assets/BoardRoom1/br10.jpg")


with col2:
    st.image("./assets/BoardRoom1/br6.jpg")
    st.image("./assets/BoardRoom1/br7.jpg")
    st.image("./assets/BoardRoom1/br8.jpg")
    st.image("./assets/BoardRoom1/br9.jpg")


with col3:
    st.image("./assets/BoardRoom1/br11.jpg")
    st.image("./assets/BoardRoom1/br12.jpg")
    st.image("./assets/BoardRoom1/br13.jpg")
    st.image("./assets/ServerRoom/server1.jpg")


with col4:
    st.image("./assets/ServerRoom/server3.jpg")
    st.image("./assets/ServerRoom/server4.jpg")
    st.image("./assets/ServerRoom/server5.jpg")
    st.image("./assets/ServerRoom/server2.jpg")

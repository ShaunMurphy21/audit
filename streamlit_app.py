import pickle
from pathlib import Path
from forms.contact  import raccess



import streamlit as st
import streamlit_authenticator as stauth # pip install streamlit-authenticator--- running version 0.1.5


from generate_key import file_path, hashed_passwords

#use pip install streamlit-authenticator==0.1.5 to download this version
# --- Page Setup ---- #

###this will run on all pages##
st.logo("assets/OIP (1).jfif")
st.sidebar.text("Made by Joseph Murphy")

# -----  USER AUTHENTICATION --------#
names = ["admin", "ASL"]
usernames = ["admin", "ASL"]

#-- loads encrypted passwords
file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
        "HC ASL", "abcdef", cookie_expiry_days=1)
name, authentication_status, username = authenticator.login("login", "main")
# ---- Chech if authenticated
@st.dialog("Request access")
def rAccess():
    raccess()


if authentication_status == False:
    st.error("Username or Password is incorrect")
    if st.button("Request Access"):
        rAccess()


if authentication_status == None:
    st.warning("Please enter your username and password")
    if st.button("Request Access"):
        rAccess()

if authentication_status:



    Home_page = st.Page(

        page = "views/HomePage.py",
        title="Home Page",
        icon= ":material/home:",
        default = True,
    )



    Annie_page = st.Page(
        page="views/Annie.py", #where page is located
        title="Annie's Desk", #Title
        icon =":material/deskphone:", #Icon of page

    )


    project_1_page = st.Page(
        page="views/boardroom.py",
        title="BoardRoom & Server",
        icon= ":material/deskphone:",

    )

    project_2_page = st.Page(
        page = "views/hayley.py",
        title = "Hayley",
        icon = ":material/deskphone:",
    )

    project_3_page = st.Page(
        page="views/Mel.py",
        title="Mel",
        icon=":material/deskphone:"


    )

    Eleanor = st.Page(
        page="views/Eleanor.py",
        title="Eleanor",
        icon=":material/deskphone:"



    )

    Glenn = st.Page(
        page="views/Glenn.py",
        title="Glenn",
        icon=":material/deskphone:"

    )

    CustomerService = st.Page(
        page="views/CustomerService.py",
        title = "Customer Service",
        icon = ":material/deskphone:"
    )


    IT = st.Page(
        page="views/It.py",
        title="IT",
        icon=":material/deskphone:"
    )
    Jason = st.Page(
        page="views/Jason.py",
        title="Jason",
        icon=":material/deskphone:"
    )
    Nick = st.Page(
        page="views/Nick.py",
        title="Nick",
        icon=":material/deskphone:"
    )
    Ken = st.Page(
        page="views/Ken.py",
        title="Ken",
        icon=":material/deskphone:"
    )

    David = st.Page(
        page="views/David.py",
        title="David",
        icon = ":material/deskphone:"
    )

    SuartSteve = st.Page(
        page="views/StuartSteve.py",
        title="Stuart and Steve",
        icon=":material/deskphone:"
    )
    Ollie = st.Page(
        page="views/Ollie.py",
        title="Ollie",
        icon=":material/deskphone:"
    )
    Spare = st.Page(
        page="views/Spare.py",
        title="Spare Desk",
        icon=":material/deskphone:"


    )
    Russel = st.Page(

        page="views/Russel.py",
        title="Russel",
        icon=":material/deskphone:"
    )


    Desk5 = st.Page(

        page="views/Desk5.py",
        title="Desk 5 Spare",
        icon = ":material/deskphone:"
    )

    Desk6 = st.Page(
        page="views/Desk6.py",
        title= "Desk 6 Spare",
        icon = ":material/deskphone:"

    )

    Desk7 = st.Page(
        page="views/Desk7.py",
        title="Desk 7 Spare",
        icon = ":material/deskphone:"


    )
    Desk8 = st.Page(

        page="views/Desk8.py",
        title="Desk 8 Spare",
        icon = ":material/deskphone:"
    )

    Susan = st.Page(
        page = "views/Susan.py",
        title = "Susan",
        icon = ":material/deskphone:"


    )

    Tyley = st.Page(
        page = "views/Tyley.py",
        title = "Tyley",
        icon = ":material/deskphone:"

    )


    #----- Navigation SETUP [Without Sections] -------- #
    #pg = st.navigation(pages=[Annie_page, project_1_page, project_2_page, project_3_page])
    #--- RUN NAVIGATION
    authenticator.logout("Logout","sidebar")
    st.sidebar.title(f"Welcome {name}")
    pg= st.navigation(
        {
            "Home Page": [Home_page],
            "Peoples Desk": [Annie_page, project_1_page, project_2_page, project_3_page, David,
                             Eleanor, Glenn, IT, Jason, Ken, Nick, SuartSteve,
                             Ollie, Russel, Spare, Susan, Tyley,
                             CustomerService, Desk5, Desk6, Desk7, Desk8,]

        }


    )
    pg.run()




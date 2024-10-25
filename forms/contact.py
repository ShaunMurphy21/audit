import re
from http.client import responses

import streamlit as st
import requests


WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZkMDYzZTA0MzE1MjY0NTUzZDUxMzIi_pc"

def is_valid_email(email):
    #checks if email is valid
    email_pattern = r"^[a-zA-Z0-9_+-]+@[A-Za-z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def raccess():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_input("Reason for access:")
        submit_button = st.form_submit_button("Submit")


        if submit_button:
            if not WEBHOOK_URL:
                st.error(
                    "Email service is not setup. Please tr again later.")
                st.stop()
            if not name:
                st.error("Please provide your name")
                st.stop()
            if not email:
                st.error("Please provide your email addresss")
            if not is_valid_email(email):
                st.error("Please provide a valid email address")
                st.stop()
            if not message:
                st.error("Please provide a reason")
                st.stop()

            #prepares data and sends it
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message has been sent successfully!🎊")
            else:
                st.error("There was an error sending your message.❌")


            st.success("Successfully Sent")
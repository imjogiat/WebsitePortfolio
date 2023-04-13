import streamlit as smt
from portfolio_email import send_email

#sets the page as wide to allowa better view
smt.set_page_config(layout="wide")

smt.title("Contact Us")

with smt.form(key="email_form"):
    user_email_addr= smt.text_input("Your email address")
    raw_message= smt.text_area("Your message")
    email_message=f"""\
    Subject: New email from {user_email_addr}
    From: {user_email_addr}
    {raw_message} 
    """

    submit_email= smt.form_submit_button("Submit")
    
    if submit_email:
        send_email(email_message)
        smt.info("Your email was successfully sent!")



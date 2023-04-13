import smtplib
import ssl
"""
Code for sending an single email using a gmail email address and client.
Can re-use as needed.
"""
def send_email(user_message):
    #This is the host and port of the email server that you're using
    host= "smtp.gmail.com"
    port=465

    email_address= "imjogiat@gmail.com"
    password= "nvyvtkimzggvnaft"
    receiver_email_address="imjogiat@gmail.com"

    #FOr the subject of the email, you have to do a backslash on previous line and Suject: ssdasd

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(email_address, password)
        server.sendmail(email_address, receiver_email_address, user_message)
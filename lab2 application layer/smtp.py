import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = "kuarshreshthasingh@gmail.com"
    receiver = "shreshthasingh6030@gmail.com"
    password = "ogas sguu ntko yvoy"   

    msg = MIMEText("Hello Kulshreshtha, this is a test email via Mailtrap.")
    msg["Subject"] = "this is just for practice purpodse please ignore"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error:", e)

send_email()

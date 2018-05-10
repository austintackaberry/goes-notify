# test to make sure i can actually send email

import smtplib
from email.mime.text import MIMEText
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587

SMTP_USERNAME = os.environ["YAHOO_USERNAME"]
SMTP_PASSWORD = os.environ["YAHOO_PASSWORD"]
EMAIL_FROM = os.environ["YAHOO_EMAIL"]
EMAIL_TO = os.environ["GMAIL_EMAIL"]

EMAIL_SUBJECT = "heyyyy"
co_msg = "hi"
def send_email():
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send_email()
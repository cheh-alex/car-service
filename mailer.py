import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class Mailer:
    def __init__(self, host, port, email, password):
        self.email = email
        self.mail = smtplib.SMTP(host, port)
        self.mail.starttls()
        self.mail.login(email, password)

    def send_text_message(self, to, subject, text):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to
        msg['Subject'] = subject
        txt = MIMEText(text)
        msg.attach(txt)

        self.mail.sendmail(self.email, to, msg.as_string())

    def send_html_message(self, to, subject, markup):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to
        msg['Subject'] = subject
        txt = MIMEText(markup, 'html')
        msg.attach(txt)
        self.mail.sendmail(self.email, to, msg.as_string())




import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "udzetrvewswna@gmail.com"
        self.password = "1j&9L6K$Hg%yK"

    def send(self, emails):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            mail = MIMEMultipart('alternative')
            mail['Subject'] = "smtpApp Test"
            mail['From'] = self.sender_mail
            mail['To'] = email

            text_template = "Mathematical Thoughts"

            "Hi {0}, This is a Test from smtpApp in Python"

            html_template =  "<h1>Mathematical Thoughts</h1>"

            "<p>Hi {0},</p>" 
            "<p>This is a Test from smtpApp in Python</p>"

            html_template = MIMEText(html_template.format(email.split("@")[0]), 'html') 
            text_template = MIMEText(text_template.format(email.split("@")[0]), 'plain')

            mail.attach(text_template)
            mail.attach(html_template)

            service.sendmail(self.sender_mail, email, mail.as_string())

        service.quit()

if __name__ == '__main__':
    mails = input("Enter emails: ").split()

    mail = Mail()
    mail.send(mails)
#import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#create message object instance
msg = MIMEMultipart()

message = "smtp Method Test"

#setup the parameters of the message
password = "1j&9L6K$Hg%yK"
msg['From'] = "zwvaatwjsgdcs@gmail.com"
msg['To'] = "udzetrvewswna@gmail.com"
msg['Subject'] = "Test Message by smtp Method"

#add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

#Login Credentials for sending the mail
server.login(msg['From'], password)

#send the message via the server
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print ("successfully sent email %s:" %(msg['To']))

#success code
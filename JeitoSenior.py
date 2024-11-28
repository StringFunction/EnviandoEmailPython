import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
try:
    servidor =  smtplib.SMTP("smtp.gmail.com", 587) #CONECTANDO AO SERVIDOR EMAIL
    servidor.starttls() #INCIANDO CRIPTOGRAFIA LS
    servidor.ehlo() #ISSO AQUI É OPCIONAL
    servidor.login
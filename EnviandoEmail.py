import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
try:
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login("franciscoclecioti@gmail.com", os.getenv("SENHA"))
    servidor.sendmail("franciscoclecioti@gmail.com", "cleciolimalive@gmail.com", 'Subject: So \
long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
    print(servidor)
except Exception as e:
    print(e)

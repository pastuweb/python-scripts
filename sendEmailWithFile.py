#!/usr/bin/python

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib
import os
 
mittente = "server@appuntivari.net"
destinatario = "francesco.pasturenzi@gmail.com"
oggetto = "AppuntiVari.net - Rischieste di informazioni"
 
try:
        msg = MIMEMultipart()
        msg.attach(MIMEText(file("/home/documenti/allegatoRichieste.txt").read()))
        msg["From"] = mittente
        msg["To"] = destinatario
        msg["Subject"] = oggetto
 
        # to send
        mailer = smtplib.SMTP()
        mailer.connect()
        mailer.sendmail(mittente, destinatario, msg.as_string())
        mailer.close()
 
        #elimina file - reset
        os.remove("/home/documenti/allegatoRichieste.txt")
 
except IOError:
        contenuto = "Nessuno HA scritto da AppuntiVari.net"
        print contenuto
        msg = MIMEText(contenuto)
        msg["From"] = mittente
        msg["To"] = destinatario
        msg["Subject"] = oggetto
        mailer = smtplib.SMTP()
        mailer.connect()
        mailer.sendmail(mittente, destinatario, msg.as_string())
        mailer.close()
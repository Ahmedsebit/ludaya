from flask import Flask
from flask_mail import Mail, Message
import os
from ludaya.ludaya import app

mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ahmedamedy@gmail.com'
app.config['MAIL_PASSWORD'] = 'osmantito88'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def send_mail(heading, sender, recepients, message):
   msg = Message(heading, sender = sender, recipients = recepients)
   msg.body = message
   mail.send(msg)
   return "Sent"

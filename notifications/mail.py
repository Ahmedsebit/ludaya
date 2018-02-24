from flask import Flask
from flask_mail import Mail, Message
import os
from decorators import async
# from ludaya.ludaya import app

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ahmedamedy@gmail.com'
app.config['MAIL_PASSWORD'] = 'osmantito88'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(heading, sender, recepients, message):
   msg = Message(heading, sender = sender, recipients = recepients)
   msg.body = message
   send_async_email(app, msg)

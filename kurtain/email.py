from flask_mail import Message
from flask import render_template
from kurtain import kurtain, mail
from threading import Thread

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Onsdagsgruppen] reset your password', sender=app.config['admins'][0], recipients=[user.email],
        text_body=render_template('email/reset_password.txt', user=user, token=token),
        html_body=render_template('email/reset_password.html', user=user, token=token))

def send_async_email(kurtain, msg):
    with kurtain.kurtain_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()
    #das
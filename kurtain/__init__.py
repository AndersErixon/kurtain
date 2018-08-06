from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail


kurtain = Flask(__name__)
kurtain.config.from_object(Config)
db = SQLAlchemy(kurtain)
migrate = Migrate(kurtain, db)
login = LoginManager(kurtain)
login.login_view = 'login'
mail = Mail(kurtain)

from kurtain import routes, models, errors

if not kurtain.debug:
    if kurtain.config['MAIL_SERVER']:
        auth = None
        if kurtain.config['MAIL_USERNAME'] or kurtain.config['MAIL_PASSWORD']:
            auth = (kurtain.config['MAIL_USERNAME'], kurtain.config['MAIL_PASSWORD'])
        secure = None
        if kurtain.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(kurtain.config['MAIL_SERVER'], kurtain.config['MAIL_PORT']),
            fromaddr='no-reply@' + kurtain.config['MAIL_SERVER'],
            toaddrs=kurtain.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        kurtain.logger.addHandler(mail_handler)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    fhand = RotatingFileHandler('logs/kurtain.log', maxBytes=10240, backupCount=10)
    fhand.setFormatter(logging.Formatter('%(asctime)s %(message)s [in %(pathname)s:%(lineno)d]'))
    fhand.setLevel(logging.INFO)
    kurtain.logger.addHandler(fhand)
    kurtain.logger.setLevel(logging.INFO)
    kurtain.logger.info('Kurtain Startup')

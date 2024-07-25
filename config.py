import os
from flask_mail import  Mail, Message
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER') 
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_SENDER')
    ADMINS = ['learn.krrish@gmail.com','krrishmahar5@gmail.com', 'krrishmahar@gmail.com']
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'es', 'hi', 'sa', 'zh', 'mr']
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') or 'http://localhost:9200'



# Flask uses Python's logging package to write its logs, and this package already has the ability to send logs by email. 
# we only need to use SMTP handler to use that feature of python

from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
import os
from flask_migrate import Migrate
from flask_mail import Mail,Message
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user


app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = 'static/uploads'
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:yusif@localhost:5432/data'
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ksbodoegarfpkk:91cf7e3db19414e1330896542c9e287e33d9e3bfa7b510db4526a0a8e758c52e@ec2-3-233-43-103.compute-1.amazonaws.com:5432/d521jpnfv0cghm'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "yusifosmanov475@gmail.com"
app.config['MAIL_PASSWORD'] = "osmanov91861001"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
db=SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"



from models import *
migrate = Migrate(app, db)
#app routes
from app.routes import *

#admin routes
from admin.routes import *

if __name__ == '__main__':
    app.run()
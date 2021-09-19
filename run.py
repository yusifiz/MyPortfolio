from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_mail import Mail,Message
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user


app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "yusifosmanov475@gmail.com"
app.config['MAIL_PASSWORD'] = "osmanov91861001"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
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
    app.run(port=5000,debug=True)
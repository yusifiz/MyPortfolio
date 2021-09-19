from flask_login.mixins import UserMixin
from run import db

class Skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skill_name = db.Column(db.String(50))
    skill_url = db.Column(db.String(250))
    skill_img = db.Column(db.String(150))

class Projects(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_name = db.Column(db.String(50))
    project_url = db.Column(db.String(250))
    project_img = db.Column(db.String(150))
    date = db.Column(db.Date)

class Feedbacks(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String(50))
    feedback = db.Column(db.Text)
    person_img = db.Column(db.String(150))
    

class Blogs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_name = db.Column(db.String(50))
    blog_url = db.Column(db.String(250))
    blog_dateTime = db.Column(db.String(70))
    blog_img = db.Column(db.String(150))
    date = db.Column(db.Date)

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_name = db.Column(db.String(50))
    contact_email = db.Column(db.String(100))
    message = db.Column(db.Text)

class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    prof_name = db.Column(db.String(50))
    prof_age = db.Column(db.String(10))
    prof_phone = db.Column(db.String(20))
    prof_email = db.Column(db.String(100))
    prof_address = db.Column(db.String(100))
    about_text = db.Column(db.Text)
    hello_text = db.Column(db.Text)

class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    edu_name = db.Column(db.String(100))
    edu_start_date = db.Column(db.String(10))
    edu_finish_date = db.Column(db.String(10))
    edu_content = db.Column(db.String(150))

class Login(UserMixin ,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)
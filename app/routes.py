#app/routes

from run import app
from flask import Flask,redirect,url_for,render_template,request


@app.route("/")
def portfolio():
    from models import Skills
    from models import Projects
    from models import Contact
    from models import Blogs
    from models import Feedbacks
    from models import Profile
    from models import Education
    skills = Skills.query.all()
    projects = Projects.query.all()
    messages = Contact.query.all()
    blogs = Blogs.query.all()
    fb = Feedbacks.query.all()
    prof = Profile.query.get(1)
    education = Education.query.all()
    return render_template("app/index.html", skills=skills, projects=projects, messages=messages, blogs=blogs, fb=fb, prof=prof, education=education)


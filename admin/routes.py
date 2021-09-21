#admin/routes

from run import app
from flask import Flask,flash,redirect,url_for,render_template,request
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager

# login

@login_manager.user_loader
def load_user(user_id):
    from models import Login
    return Login.query.get(int(user_id))

@app.route("/login",methods=["GET","POST"])
def admin_login():
    from models import Login
    from run import db
    login = Login(
        admin_username = "Yusif",
        admin_password = "qizilmezun",
        log_bool = False
    )
    db.session.add(login)
    db.session.commit()
    
    if request.method == "POST":
        if login.admin_username == request.form["admin_username"] and login.admin_password == request.form["admin_password"]:
            login_user(login, remember=login.log_bool)
            return redirect (url_for("profile"))

        else:
            flash ("Username or password is wrong!")
            return redirect(url_for("admin_login"))

    return render_template("admin/login.html", login = login)


@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect (url_for("portfolio"))

# Admin Profile

@app.route("/admin", methods=["GET","POST"])
@login_required
def profile():
    from models import Profile
    from run import db
    
    prof = Profile(
        prof_name = "Yusif Osmanov_",
        prof_age = "19",
        prof_phone = "+994 55 782 91 86",
        prof_email = "osmanov.yusif@gmail.com",
        prof_address = "Sumqayıt, Azərbaycan",
        hello_text = "Mən Yusif Osmanov, uşaqlıqdan bəri həvəs göstərdiyim bu sahəyə, 19 yaşında professional olaraq başlamışam. Pragmatech Təshil və İnkişaf Mərkəzində Kərimov Samir müəllimin vasitəsilə, veb development sahəsini öyrənirəm. HTML, CSS, BootStrap, JavaScript, Git & GitHub biliklərim var. Bütün cihaz ekranları üçün yaradıcı və yüksək səviyyəli veb saytlar hazırlayıram.",
        about_text = "2019-cu ildə qəbul olduğum Bakı Dövlət Universitetində 3-cü kurs tələbəsiyəm. Tətbiqi riyaziyyat və Kibernetika fakültəsinin, kompüter elmləri ixtisasında təhsil alıram. Fərqli kurslar vasitəsilə və öz üzərimdə çalışaraq, intermediate ingilis dili səviyyəsinə yiyələnmişəm. Pragmatech Təshil və İnkişaf Mərkəzində veb development sahəsini professional şəkildə öyrənməyə başlamışam. Daim özümü inkişaf etdirməyə və yeni şeylər öyrənməyə həvəsliyəm."
    )
    db.session.add(prof)
    db.session.commit()
    if request.method=='POST':
        
        
        prof=Profile.query.get(1)
        
        prof.prof_name=request.form['prof_name']
        prof.prof_age=request.form['prof_age']
        prof.prof_phone=request.form['prof_phone']
        prof.prof_email=request.form['prof_email']
        prof.prof_address=request.form['prof_address']
        prof.about_text = request.form["about_text"]
        prof.hello_text = request.form["hello_text"]
        db.session.commit()
        return redirect('/')    
    return render_template("admin/profile.html", prof = Profile.query.get(1))

# Admin Skills

@app.route("/admin/skills",methods=["GET","POST"])
@login_required
def skills():
    from models import Skills
    import os
    from run import db
    from werkzeug.utils import secure_filename
    skills = Skills.query.all()
    if request.method=="POST":
        file = request.files['skill_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        skill_name = request.form["skill_name"]
        skill_url = request.form["skill_url"]
        skl= Skills(
            skill_name=skill_name,
            skill_url=skill_url,
            skill_img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        )
        db.session.add(skl)
        db.session.commit()
        return redirect("/")
    return render_template("admin/skills.html", skills=skills)

@app.route("/skillDelete/<int:id>", methods=["GET","POST"])
@login_required
def skill_delete(id):
    from models import Skills
    from run import db
    import os
    skills = Skills.query.filter_by(id=id).first()
    
    filename = skills.skill_img
    os.unlink(os.path.join(filename))
    db.session.delete(skills)
    db.session.commit()
    return redirect ("/admin/skills")

@app.route("/skillUpdate/<int:id>", methods= ["GET","POST"])
@login_required
def skill_update(id):
    from models import Skills
    from run import db
    
    skills = Skills.query.filter_by(id=id).first()
    if request.method== "POST":
        skills = Skills.query.filter_by(id=id).first()
        skills.skill_name = request.form["skill_name"]
        skills.skill_url = request.form["skill_url"]

        db.session.commit()
        return redirect("/")
    return render_template("admin/update_skill.html", skills=skills)

# Admin Projects

@app.route("/admin/projects",methods=["GET","POST"])
@login_required
def projects():
    from models import Projects
    import os
    from run import db
    from werkzeug.utils import secure_filename
    from datetime import date
    projects = Projects.query.all()
    if request.method=="POST":
        current = date.today()
        file = request.files['project_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        project_name = request.form["project_name"]
        project_url = request.form["project_url"]
        prjct= Projects(
            project_name=project_name,
            project_url=project_url,
            project_img = os.path.join(app.config['UPLOAD_FOLDER'], filename),
            date = current
        )
        db.session.add(prjct)
        db.session.commit()
        return redirect("/")
    

    return render_template("admin/projects.html",projects=projects)

@app.route("/projectDelete/<int:id>", methods=["GET","POST"])
@login_required
def project_delete(id):
    from models import Projects
    from run import db
    import os
    projects = Projects.query.filter_by(id=id).first()
    filename = projects.project_img
    os.unlink(os.path.join(filename))
    
    db.session.delete(projects)
    db.session.commit()
    return redirect ("/admin/projects")

@app.route("/projectUpdate/<int:id>", methods= ["GET","POST"])
@login_required
def project_update(id):
    from models import Projects
    from run import db
    
    projects = Projects.query.filter_by(id=id).first()
    if request.method== "POST":
        projects = Projects.query.filter_by(id=id).first()
        projects.project_name = request.form["project_name"]
        projects.project_url = request.form["project_url"]
        db.session.commit()
        return redirect("/")
    return render_template("admin/update_project.html", projects=projects)

# Admin Contact

@app.route("/admin/contact", methods=["GET","POST"])
def contact():
    from models import Contact
    from run import db
    import smtplib
    from flask_mail import Mail, Message
    from run import mail
    messages = Contact.query.all()
    if request.method == "POST":
        contact_name = request.form["contact_name"]
        contact_email = request.form["contact_email"]
        message = request.form["message"]
        cnt = Contact(
            contact_name = contact_name,
            contact_email = contact_email,
            message = message
        )
        msg = cnt.message
        # server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.starttls()
        # server.login("yusifosmanov475@gmail.com", "osmanov91861001")
        # server.sendmail("yusifosmanov475@gmail.com", cnt.contact_email, msg)    
        

        msg = Message(message, sender = contact_email, recipients = ["yusifosmanov475@gmail.com"])
        mail.send(msg)

        flash('<h5>Mesaj Göndərildi..</h5>')
        db.session.add(cnt)
        db.session.commit()
        return redirect ("/")
    return render_template("admin/contact.html", messages=messages)

@app.route("/contactDelete/<int:id>")
@login_required
def contact_delete(id):
    from models import Contact
    from run import db
    messages = Contact.query.filter_by(id=id).first()
    db.session.delete(messages)
    db.session.commit()
    return redirect ("/admin/contact")

# Admin Blog

@app.route("/admin/blog", methods=["GET","POST"])
@login_required
def blog():
    from models import Blogs
    import os
    from run import db
    from werkzeug.utils import secure_filename
    from datetime import date
    blogs = Blogs.query.all()
    if request.method == "POST":
        current = date.today()
        file = request.files['blog_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog_name = request.form["blog_name"]
        blog_url = request.form["blog_url"]
        blog_dateTime = request.form["blog_dateTime"]
        blg = Blogs(
            blog_name = blog_name,
            blog_url = blog_url,
            blog_dateTime = blog_dateTime,
            blog_img = os.path.join(app.config['UPLOAD_FOLDER'], filename),
            date=current
        )
        db.session.add(blg)
        db.session.commit()
        return redirect ("/")
    return render_template("admin/blog.html", blogs=blogs)

@app.route("/blogDelete/<int:id>", methods=["GET","POST"])
@login_required
def blog_delete(id):
    from models import Blogs
    from run import db
    import os
    blogs = Blogs.query.filter_by(id=id).first()
    filename = blogs.blog_img
    os.unlink(os.path.join(filename))
    db.session.delete(blogs)
    db.session.commit()
    return redirect ("/admin/blog")

@app.route("/blogUpdate/<int:id>", methods = ["GET","POST"])
@login_required
def blog_update(id):
    from models import Blogs
    from run import db
    blogs = Blogs.query.filter_by(id=id).first()
    if request.method== "POST":
        blogs = Blogs.query.filter_by(id=id).first()
        blogs.blog_name = request.form["blog_name"]
        blogs.blog_url = request.form["blog_url"]
        blogs.blog_dateTime = request.form["blog_dateTime"]
        db.session.commit()
        return redirect("/")
    return render_template("admin/update_blog.html", blogs=blogs)

# Admin FeedBacks

@app.route("/admin/feedbacks", methods=["GET","POST"])
@login_required
def feedbacks():
    from models import Feedbacks
    import os
    from run import db
    from werkzeug.utils import secure_filename
    fb = Feedbacks.query.all()
    if request.method == "POST":
        file = request.files['person_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        full_name = request.form["full_name"]
        feedback = request.form["feedback"]
        fbcks = Feedbacks(
            full_name = full_name,
            feedback = feedback,
            person_img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        )
        db.session.add(fbcks)
        db.session.commit()
        return redirect("/")
    return render_template("admin/feedbacks.html", fb=fb)

@app.route("/feedbacksDelete/<int:id>", methods=["GET","POST"])
@login_required
def feedbacks_delete(id):
    from models import Feedbacks
    from run import db
    import os
    fb = Feedbacks.query.filter_by(id=id).first()
    filename = fb.person_img
    os.unlink(os.path.join(filename))
    db.session.delete(fb)
    db.session.commit()
    return redirect ("/admin/feedbacks")


@app.route("/feedbacksUpdate/<int:id>", methods=["GET","POST"])
@login_required
def feedbacks_update(id):
    from models import Feedbacks
    from run import db
    fb = Feedbacks.query.filter_by(id=id).first()
    if request.method== "POST":
        fb = Feedbacks.query.filter_by(id=id).first()
        fb.full_name = request.form["full_name"]
        fb.feedback = request.form["feedback"]
        
        db.session.commit()
        return redirect("/")
    return render_template("admin/update_feedbacks.html", fb=fb)    

# Admin Education

@app.route("/admin/education", methods=["GET","POST"])
@login_required
def education():
    from models import Education
    from run import db
    education = Education.query.all()
    if request.method == "POST":
        edu_name = request.form["edu_name"]
        edu_start_date = request.form["edu_start_date"]
        edu_finish_date = request.form["edu_finish_date"]
        edu_content = request.form["edu_content"]
        edu = Education(
            edu_name = edu_name,
            edu_start_date = edu_start_date,
            edu_finish_date = edu_finish_date,
            edu_content = edu_content
        )
        db.session.add(edu)
        db.session.commit()
        return redirect("/")
    return render_template("admin/education.html", education=education)

@app.route("/educationDelete/<int:id>")
@login_required
def education_delete(id):
    from models import Education
    from run import db
    education = Education.query.filter_by(id=id).first()
    db.session.delete(education)
    db.session.commit()
    return redirect ("/admin/education")


@app.route("/educationUpdate/<int:id>", methods=["GET","POST"])
@login_required
def education_update(id):
    from models import Education
    from run import db
    education = Education.query.filter_by(id=id).first()
    if request.method== "POST":
        education = Education.query.filter_by(id=id).first()
        education.edu_name = request.form["edu_name"]
        education.edu_start_date = request.form["edu_start_date"]
        education.edu_finish_date = request.form["edu_finish_date"]
        education.edu_content = request.form["edu_content"]
        db.session.commit()
        return redirect("/")
    return render_template("admin/update_education.html", education=education)    
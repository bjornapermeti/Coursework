from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from passlib.hash import sha256_crypt
from datetime import datetime

engine = create_engine("mysql://root:bjorna2002@localhost/register")           #put the information in a databse
                        #(mysql+pymysql://username:password@localhost/databasename)
db=scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)

#class Todo(db.Model):
    #id = db.Column(db.Integer)

@app.route("/")
def home():
    return render_template("home.html")

#register form

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        secure_password = sha256_crypt.encrypt(str(password))
        email = request.form.get("email")

        if password == confirm:     #we submit the form if the password is the same as the confirm    
            db.execute("INSERT INTO users(name, username, password, email) VALUES(:name,:username,:password,:email)",
                                         {"name":name,"username":username,"password":secure_password,"email":email})
            db.commit()
            flash("you are registered and can login","success")
            return redirect(url_for('login'))
        else:
            flash("password does not match","danger")
            return render_template("register.html")

    return render_template("register.html")

#login

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
         username = request.form.get("username")
         password = request.form.get("password")

         usernamedata = db.execute("SELECT username FROM users WHERE username=:username",{"username":username}).fetchone()
         passwordata = db.execute("SELECT password FROM users WHERE username=:username",{"username":username}).fetchone()

         if usernamedata is None:
             flash("No username", "danger")
             return render_template("login.html")
         else:
             for passwor_data in passwordata:
                 if sha256_crypt.verify(password,passwor_data):
                     session["log"]= True

                     flash("You are now login", "success")
                     return redirect(url_for('photo'))
                 else:
                     flash("incorrect password","danger")
                     return render_template("login.html")

    return render_template("login.html")

#photo
@app.route("/photo")
def photo():
    return render_template("photo.html")


#logout
@app.route("/logout")
def logout():
    session.clear()
    flash("You are now logged out", "success")
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.secret_key="coursework123"
    app.run(debug=True)
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
            db.execute("INSERT INTO users(name, username, email) VALUES(:name,:username,:email)",
                                         {"name":name,"username":username,"email":email})
            db.commit()
            return redirect(url_for('login'))
        else:
            flash("password does not match","danger")
            return render_template("register.html")

    return render_template("register.html")

#login

@app.route("/login")
def login():
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
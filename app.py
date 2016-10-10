from flask import Flask, render_template, request, session, url_for
import hashlib

app = Flask(__name__)    #create Flask object
app.secret_key = "lmao"

d={}
user=""

@app.route("/")
def home():
    convertDict()
    if(user in session):
        return welcome()
    else:
        return login()
        
    
@app.route("/login/", methods=["POST"])
def login():
    return render_template( 'login.html',message="Bienvenido!" )

                
@app.route("/auth/", methods=["POST"])
def authenticate():
    global user
    convertDict()
    if request.method=="POST":
        u=request.form["username"]
        user=u
        p=hashbrowns(request.form["pass"])
        if u in d.keys():
            if p==d[u][:56]:
                session[user]=p
                return welcome()
            else:
                return render_template("login.html",message="Hmm... it seems that your password was incorrect. try again.")
        else:
            return render_template("login.html",message="Hmm... that username doesn't seem to exist.")
        return "YES"


@app.route("/register/",methods=["POST"])
def registration():
    if request.method=="POST":
        u=request.form["username"]
        p=hashbrowns(request.form["pass"])
        if u in d.keys():
            return render_template("login.html",message="Hmm... that username is already taken. try a different one.")
        else:
            if len(u) < 1 or len(p) < 1:
                return render_template("login.html",message="Hmm... please enter a valid username and password")
            else:
                addAccount(u,p)
                convertDict()
                return render_template("login.html",message="Success! Your account has been created.")
        return "YES"

@app.route("/welcome/",methods=["POST"])
def welcome():
    return render_template("loggedin.html", message="you made it, "+user+"!")

@app.route("/other/")
def other():
    if(user in session):
        return render_template("other.html", message="you are logged in as "+user+".")
    else:
        return render_template("other.html", message="you are not logged in")


@app.route("/logout/",methods=["POST"])
def logout():
    if(user in session):
        session.pop(user)
    return home()

def convertDict():
    f = open("data/accounts.csv")
    f.readline()
    m = f.readline()
    while m!='':
        n = m.index(',')+1 # finds index of second "
        d[m[:n-1]] = m[n:]
        m = f.readline() # next line, por favor
    return d

def hashbrowns(m):
    return hashlib.sha224(m).hexdigest()

def addAccount(u,p):
    fd = open('data/accounts.csv','a')
    fd.write(u+","+p+"\n")
    fd.close()
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

from flask import Flask, render_template, request
import hashlib
app = Flask(__name__)    #create Flask object

d={}

@app.route("/")
def home():
    convertDict()
    return render_template( 'login.html',message="Bienvenido!" )


@app.route("/auth", methods=["POST"])
def authenticate():
    convertDict()
    if request.method=="POST":
        u=request.form["username"]
        p=hashbrowns(request.form["pass"])
        if u in d.keys():
            if p==d[u][:56]:
                return render_template("loggedin.html", message="you made it!")
            #elif len(p) != len(d[u]):
            #    return render_template("loggedin.html", message=len(d[u]))
            else:
                return render_template("login.html",message="Hmm... it seems that your password was incorrect. try again.")
        else:
            return render_template("login.html",message="Hmm... that username doesn't seem to exist.")
        return "YES"


@app.route("/register",methods=["POST"])
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



    '''
    if request.method=="POST":
        u=request.form["username"]
        p=hashbrowns(request.form["pass"])
        
        log=request.form["log"]
        reg=request.form["reg"]
        if u in d.keys():
            if log:
                if p==d[u]:
                    return render_template("loggedin.html", message="you made it!")
                else:
                    return render_template("login.html",message="Hmm... it seems that your password was incorrect. try again.")
            elif reg:
                return render_template("login.html",message="Hmm... that username is already taken. try a different one.")
        else:
            if log:
                return render_template("login.html",message="Hmm... that username doesn't seem to exist.")
            elif reg:
                if len(u) < 1 or len(p) < 1:
                    return render_template("login.html",message="Hmm... please enter a valid username and password")
                else:
                    addAccount(u,p)
                    convertDict("data/accounts.csv")
                    return render_template("login.html",message="Success! Your account has been created.")
        return "YES"

'''

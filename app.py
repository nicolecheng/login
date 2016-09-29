from flask import Flask, render_template, request
app = Flask(__name__)    #create Flask object


@app.route("/")
def home():
    return render_template( 'login.html',success="Bienvenido!" )


@app.route("/auth", methods=["POST"])
def authenticate():
    if request.method=="POST":
        if request.form["username"]=="undercover" and request.form["pass"]=="martyn":
            return render_template("loggedin.html", user=request.form["username"], success="you made it!")
        else:
            return render_template("login.html",success="Hmm... Something was wrong. Try again.",\
            mas="psst try this: [undercover,martyn]")
    return "Waaaa hooo HAAAH"


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

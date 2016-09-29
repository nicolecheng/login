from flask import Flask, render_template, request
app = Flask(__name__)    #create Flask object


@app.route("/")
def home():
    '''
    print "\n\n\n"
    print "***DIAG: this Flask obj ***"
    print app
    print "***DIAG: request obj ***"
    print request
    print "***DIAG: request.args ***"
    print request.args
    #print "***DIAG: request.args['username']  ***"
    #print request.args['username'] #only works if username submitted
    #print "***DIAG: request.headers ***"
    #print request.headers          #only works for POST
'''
    return render_template( 'login.html',success="Bienvenido!" )


@app.route("/auth", methods=["POST"])
def authenticate():
    '''
    print "\n\n\n"
    print "***DIAG: this Flask obj ***"
    print app
    print "***DIAG: request obj ***"
    print request
    print "***DIAG: request.args ***"
    print request.args
    #print "***DIAG: request.args['username']  ***"
    #print request.args['username'] #only works if username submitted
    #print "***DIAG: request.headers ***"
    #print request.headers          #only works for POST
'''
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



    #######
'''

@app.route("/")
def root():
       #only works for POST
    return render_template("index.html")

@app.route("/auth", methods=["GET", "POST"])
def ausdg():
        #print "***DIAG: this Flask obj ***"
        #print app
        #print "***DIAG: request obj ***"
        #print request

        if request.method=="POST":
            if request.form["username"]=="Kathy" and request.form['pazz']=="123":
                return render_template("success.html", user=request.form["username"])
            else:
                return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
'''

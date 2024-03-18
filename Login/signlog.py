from flask import Flask,render_template,session,request
apk=Flask(__name__)
apk.secret_key="rv"

@apk.route("/",methods=["GET","POST"])
def sign():
    if request.method=="POST":
        a=request.form["rname"]
        b=request.form["rnum"]
        c=request.form["rmail"]
        d=request.form["rpas"]
        session['rname']=a
        session['rnum']=b
        session['rmail']=c
        session['rpas']=d

        
        return render_template("signsucc.html")
    
    else:
        return render_template("signin.html") 
    

@apk.route("/login",methods=["GET","POST"])
def loginout():
    if request.method=="POST":
        ases=request.form["iname"]
        bses=request.form["ipas"]

        if ases==session['rname'] and bses==session['rpas']:
            return "LOGIN SUCCESSFULL"
        
        else:
            return "LOGIN FAILED...!    INVALID USER NAME OR PASSWORD"
        
    else:
        return render_template("login.html")


if __name__=="__main__":
    apk.run(debug=True)
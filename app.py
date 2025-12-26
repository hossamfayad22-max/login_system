from flask import Flask,request,render_template
import random
import string
import database
alpha=string.ascii_letters+string.digits+string.punctuation+" "
alpha=list(alpha)
shuffled=alpha.copy()
random.shuffle(shuffled)


app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def homeo():
    return render_template('index.html')

@app.route("/signup",methods=["GET","POST"])
def home():
    if request.form.get('username'):
        username = request.form.get('username')
        database.user_names.append(username)
    if request.form.get('password'):
        password=request.form.get('password')
        enc_pass=""
        for i in password:
            enc_pass+=shuffled[alpha.index(i)]
        database.passwords.append(enc_pass)
    print("added")
    return render_template('signup.html')


@app.route("/signin",methods=["GET","POST"])
def homee():
    if request.method == "POST":
        u=request.form.get('usernamee')
        p=request.form.get('passwordd')
        if not u or not p:
            return render_template("false.html")
        e=""
        for i in p:
                if i in alpha:
                    e+=shuffled[alpha.index(i)]    
        if e in database.passwords and u in database.user_names:
            return render_template("true.html")
        return render_template('false.html')     
    return render_template('signin.html')   
        

if __name__=="__main__":
    app.run(debug=True)
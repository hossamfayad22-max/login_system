from flask import Flask,request,render_template
import random
import string
import database
alpha=string.ascii_letters+string.digits+string.punctuation+" "
alpha=list(alpha)
shuffled=alpha.copy()
random.shuffle(shuffled)


app=Flask("__name__")
@app.route("/signup",methods=["GET","POST"])
def home():
    if request.form.get('username'):
        username = request.form.get('username')
        database.user_names.append(username)
    if request.form.get('password'):
        password=request.form.get('password')
        for i in password:
            database.passwords.append(shuffled[alpha.index(i)],end="")
    print("added")
    return render_template('signup_1.html')
        

if __name__=="__main__":
    app.run(debug=True)
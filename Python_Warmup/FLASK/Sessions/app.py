from flask import Flask,render_template,redirect,url_for,session,request

app = Flask(__name__)
app.secret_key = "shyam"
# session.permanent = True

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session['user'] = username
        return redirect(url_for("user"))
    return render_template("login.html")

@app.route('/user')
def user():
    if 'user' in session:
        name = session['user']
        return f"Your login is successfull {name}"
    else:
        return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
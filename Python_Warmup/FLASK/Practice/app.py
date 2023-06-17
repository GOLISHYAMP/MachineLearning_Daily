from flask import Flask,render_template,url_for,session,redirect,request
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "SHYAM"
app.permanent_session_lifetime = timedelta(minutes=5)
# session["user_dic"] = {}
user_pass = {}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        if user in user_pass:
            if request.form['password'] == user_pass[user]:
                session["user"] = user
                return redirect(url_for("user"))
            return f"Sorry! incorrect password"
        else:
            return redirect(url_for("signin"))
    elif "user" in session:
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/signin", methods=["POST","GET"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_pass[username] = password
        return redirect(url_for("login"))
        # print(f'{username} {user_pass[username]}')
    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("login"))

@app.route("/user")
def user():
    if "user" in session:
        name = session["user"]
        return f"You logged in as {name}"
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
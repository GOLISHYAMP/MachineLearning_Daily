from flask import Flask,render_template,url_for,session,redirect,request

app = Flask(__name__)
app.secret_key = "SHYAM"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        if request.form['password'] == 'Shyam@312000':
            session["user"] = user
            return redirect(url_for("user"))
    elif "user" in session:
        return redirect(url_for("user"))
    return render_template("login.html")

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
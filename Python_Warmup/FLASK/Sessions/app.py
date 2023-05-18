from flask import Flask,render_template,redirect,url_for,session,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("user",user= username))
    return render_template("login.html")

@app.route('/<user>')
def user(user):
    return f"Your login is successfull {user}"



if __name__ == "__main__":
    app.run(debug=True)
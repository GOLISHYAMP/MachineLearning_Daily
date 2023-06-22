from flask import Flask,render_template,redirect,session,url_for,flash,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        return render_template("login.html")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        return redirect(url_for("user", usr = user))
    return render_template("login.html")

@app.route('/<usr>')
def user(usr):
    return f"Hello {usr}"

if __name__ == "__main__":
    app.run(debug=True)
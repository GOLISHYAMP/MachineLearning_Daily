from flask import Flask,flash,render_template,url_for,redirect,request,session

app = Flask(__name__)
app.secret_key = "SHYAM"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form['username']
        flash(f"You have been successfully logined in as {user}")
        return redirect(url_for('user',un = user))
    return render_template("login.html")

@app.route("/<un>")
def user(un):
    return render_template("user.html")

if __name__ == "__main__":
    app.run(debug=True)
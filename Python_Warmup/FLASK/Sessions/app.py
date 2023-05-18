from flask import Flask,render_template,redirect,url_for,session,request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

def login():
    if request.method == "POST":
        user = request.form("username")
        return render_template(url_for("user"),user)

@app.route("/<user>")
def user:



if __name__ == "__main__":
    app.run(debug=True)
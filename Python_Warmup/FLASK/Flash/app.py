from flask import Flask, render_template, redirect, url_for, session, flash

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("home.html")

@app.route('/login')
def login():
    diff = 10
    maxi = 100
    return render_template("login.html",context=[diff,maxi])

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/atharva')
def atharva():
    return render_template("Atharva.html")
if __name__ == '__main__':
    app.run(debug=True)
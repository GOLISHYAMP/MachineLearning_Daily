from flask import Flask,render_template,redirect,session,url_for,flash

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)
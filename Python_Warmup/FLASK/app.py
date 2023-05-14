from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello this is home page, First time learning in flask"

@app.route("/courses")
def courses():
    return "Welcome to our courses"

# The below one is a dynamic routing
@app.route('/<name>')
def name(name):
    return f"Hello {name}!"

@app.route('/admin')
def admin():
    return redirect(url_for("home")) 


if __name__ == "__main__":
    app.run(debug=True)

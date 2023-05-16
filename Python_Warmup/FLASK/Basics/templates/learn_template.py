from flask import Flask, render_template,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/courses')
def courses():
    li = ['AI','DL','ML','CV']
    content = 'HELLO I AM THE CONTENT'
    return render_template('courses.html',context=[content,li])

@app.route("/admin")
def admin():    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
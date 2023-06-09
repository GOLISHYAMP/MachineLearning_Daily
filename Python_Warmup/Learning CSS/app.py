from flask import Flask,render_template,redirect,session,url_for,flash,request,jsonify
import requests,json
from datetime import timedelta, datetime

app = Flask(__name__)
user_pass = {}
app.secret_key='Shyam'
# app.permanent_session_lifetime = timedelta(seconds=30)

sessions = {
    'vinod': {
        'startTime': datetime.now(),
        'duration': timedelta(seconds=30),  # 1 hour
        # Add any other relevant session data
    }
}

@app.route('/extend-session', methods=['POST'])
def extend_session():
    session_key = request.json['sessionKey']

    # Verify session key
    if session_key not in sessions:
        return jsonify({'error': 'Session key not found'}), 404

    # Retrieve session details
    session = sessions[session_key]

    # Check session expiration
    if datetime.now() > session['startTime'] + session['duration']:
        # Session has expired, perform logout logic here
        del sessions[session_key]
        return jsonify({'message': 'Session expired. You have been logged out.'}), 401
        # Increase session time by 1 hour
    session['duration'] += timedelta(seconds=30)

    # Update session details (e.g., save to a database)

    # Return success response
    return jsonify({'message': 'Session time increased successfully'})



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in user_pass:
            if password == user_pass[username]:
                sessions[username] = {'startTime':datetime.now(),'duration':timedelta(seconds=30)}
                return redirect(url_for('user',user = username)) 
        return f'Invalid Username or password'
    return render_template("login.html")

@app.route("/signup", methods=["POST","GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["Email"]
        user_pass[username] = password
        accessTokenUrl = "http://localhost:8080/realms/firstRealm/protocol/openid-connect/token"
        #update the admin credential for your keycloak instance
        adminname='shyam'
        adminpassword='Shyam'
        audience = 'oidc_flaskapp'
        payload='client_id=admin-cli&username='+adminname+'&password='+adminpassword+'&grant_type=password'+'&audience='+audience

        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", accessTokenUrl, headers=headers, data=payload)

        access_token=json.loads(response.text)['access_token']
        # print(access_token)
        addUserUrl = "http://localhost:8080/admin/realms/firstRealm/users"
    
        # name = "usertest"
        # email = "usertest@gmail.com"
        payload="{\r\n    \"username\":\""+username+"\",\r\n    \"enabled\":true,\r\n    \"emailVerified\":true,\r\n    \"email\":\""+email+"\",    \"credentials\":[ {\r\n      \"type\": \"password\",\r\n      \"value\":\""+password+"\"\r\n    }]\r\n}"
        headers = {
            'Authorization': 'Bearer '+access_token+'',
            'Content-Type': 'application/json'
                }

        response = requests.request("POST", addUserUrl, headers=headers, data=payload)
        # print(response.text)
        if (response.status_code==201):
            return f"{username} user added successfully"
        elif (response.status_code==409):
            return f"{username} already exist in the Keycloak"
        # print(f'{username} {user_pass[username]}')
    return render_template("signup.html")

@app.route("/<user>")
def user(user):
    if user in sessions:
        session = sessions[user]
        
        if datetime.now() > session['startTime'] + session['duration']:
        # Session has expired, perform logout logic here
            del sessions[user]
            return jsonify({'message': 'Session expired. You have been logged out.'}), 401
        return f"You logged in as {user}"
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
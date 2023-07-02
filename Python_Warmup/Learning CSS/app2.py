from flask import Flask,render_template,redirect,session,url_for,flash,request,jsonify
import requests,json
from datetime import timedelta, datetime
from keycloak import KeycloakOpenID

app = Flask(__name__)
app.secret_key='Shyam'

keycloak_openid = KeycloakOpenID(server_url='http://localhost:8080/admin/',
                                client_id='oidc_flaskapp',
                                realm_name="firstRealm",
                                client_secret_key="VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1")

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # if keycloak_openid.token()
        #     if password == user_pass[username]:
        #         sessions[username] = {'startTime':datetime.now(),'duration':timedelta(seconds=30)}
        #         return redirect(url_for('user',user = username)) 
        # return f'Invalid Username or password'
        # Get authorization URL
        config_well_known = keycloak_openid.well_known()
        print(config_well_known)
        keycloak_openid.auth_url(
            redirect_uri="http://localhost:5000/cb",
            scope="email",
            state="all done"
        )
       
        # Redirect the user to the authorization URL for authentication

        # After successful authentication, retrieve the authorization code from the callback URL
        # and exchange it for an access token
        code = "authorization_code_from_callback"

        # Exchange the authorization code for tokens
        token = keycloak_openid.token(
            grant_type="authorization_code",
            code=code,
            redirect_uri="your_redirect_uri"
        )

        if 'error' in keycloak_openid.__dict__:
            # Invalid credentials, show error message
            return render_template('login.html', error='Invalid username or password')

        # Save access token and refresh token in the session
        session['token'] = keycloak_openid.token['access_token']
        session['refresh_token'] = keycloak_openid.token['refresh_token']

        return redirect('/dashboard')
    return render_template("login.html")


@app.route("/signup", methods=["POST","GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["Email"]
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
            flash(f"{username} user added successfully")
            return redirect(url_for("login"))
        
        elif (response.status_code==409):
            flash(f"{username} already exist in the Keycloak")
            return render_template("signup.html")
        # print(f'{username} {user_pass[username]}')
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, session, redirect
from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

app = Flask(__name__)
app.secret_key = 'SHYAM'  # Set a secret key for session management

keycloak_connection = KeycloakOpenIDConnection(
                        server_url="http://localhost:8080/admin",
                        username='shyam',
                        password='Shyam',
                        realm_name="master",
                        user_realm_name="firstRealm",
                        client_id="oidc_flaskapp",
                        client_secret_key="VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1",
                        verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/admin/",
                                 client_id="oidc_flaskapp",
                                 realm_name="firstRealm",
                                 client_secret_key="VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1")
# auth_url = keycloak_openid.auth_url(
#     redirect_uri="your_call_back_url",
#     scope="email",
#     state="your_state_info")
# access_token = keycloak_openid.token(
#     grant_type='authorization_code',
#     code='the_code_you_get_from_auth_url_callback',
#     redirect_uri="your_call_back_url")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        print("ALL FINE BRO")
        username = request.form.get('username')
        email = request.form.get('Email')
        password = request.form.get('password')

        print(username,email,password)
        keycloak_admin.create_user({   "username": username,
                                       "enabled": True,
                    "credentials": [{"value": password,"type": "password",}]})
       
        print("user Created")
        # Redirect to the login page
        return redirect('/login')

    # Render the registration form
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Perform Keycloak authentication
        keycloak_openid.token(username, password)

        if 'error' in keycloak_openid.__dict__:
            # Invalid credentials, show error message
            return render_template('login.html', error='Invalid username or password')

        # Save access token and refresh token in the session
        session['token'] = keycloak_openid.token['access_token']
        session['refresh_token'] = keycloak_openid.token['refresh_token']
        return redirect('/dashboard')

    # Render the login form
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # Retrieve user information from Keycloak token
    access_token = session.get('token')
    userinfo = keycloak_openid.userinfo(access_token)
    username = userinfo.get('preferred_username')
    email = userinfo.get('email')

    # Render the dashboard template
    return render_template('dashboard.html', username=username, email=email)


if __name__ == '__main__':
    app.run(debug=True)

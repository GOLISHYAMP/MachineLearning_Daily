from flask import Flask, request, redirect, url_for
from keycloak import KeycloakAdmin, KeycloakOpenID

app = Flask(__name__)

# Keycloak Configuration
keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/admin",
                              username="shyam",
                              password="Shyam",
                              realm_name="firstRealm",
                              client_id="oidc_flaskapp",
                              client_secret_key="VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1")

keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/admin",
                                client_id="oidc_flaskapp",
                                realm_name="firstRealm",
                                client_secret_key="VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1")

@app.route('/')
def index():
    return 'Welcome to the Keycloak Flask Example!'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Create user in Keycloak
        user_info = {
            "username": username,
            "email": email,
            "enabled": True,
            "credentials": [{"value": password, "type": "password"}]
        }
        keycloak_admin.create_user(user_info)

        return redirect(url_for('index'))

    return '''
    <form method="post" action="/signup">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <input type="submit" value="Sign Up">
    </form>
    '''

@app.route('/login')
def login():
    auth_url = keycloak_openid.auth_url(
        redirect_uri=url_for('callback', _external=True),
        scope="email",
        state="your_state_info"
    )
    return redirect(auth_url)

@app.route('/cb')
def callback():
    code = request.args.get('code')
    redirect_uri = url_for('callback', _external=True)
    access_token = keycloak_openid.token(
        grant_type='authorization_code',
        code=code,
        redirect_uri=redirect_uri
    )
    # Do something with the access token, like store it in session or use it for API calls
    return 'Access Token: {}'.format(access_token)

if __name__ == '__main__':
    app.run(debug=True)

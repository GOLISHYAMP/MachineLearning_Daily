from flask import Flask, redirect, url_for,request
from keycloak import KeycloakOpenID

app = Flask(__name__)

# Keycloak Configuration
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/realms/firstRealm/protocol/openid-connect/auth",
                                client_id="oidc_flaskapp",
                                realm_name="firstRealm",
                                client_secret_key="VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1")

@app.route('/')
def home():
    return 'Welcome to the Keycloak Flask Example!'

@app.route('/login')
def login():
    auth_url = keycloak_openid.auth_url(
        redirect_uri="http://localhost:8080/realms/firstRealm/protocol/openid-connect/auth?response_type=code&client_id=oidc_flaskapp",
        scope="openid",
    )
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    redirect_uri = "keycloak-oidc"
    token = keycloak_openid.token(
        grant_type='authorization_code',
        code=code,
        redirect_uri=redirect_uri
    )
    # Do something with the token, like store it in session or use it for API calls
    return 'Token: {}'.format(token)

if __name__ == '__main__':
    app.run()

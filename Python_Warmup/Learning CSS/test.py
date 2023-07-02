from flask import Flask, redirect, request, url_for
from keycloak import KeycloakOpenID, KeycloakAdmin, KeycloakOpenIDConnection

app = Flask(__name__)
app.secret_key = 'SHYAM'  # Set a secret key for session management

KEYCLOAK_SERVER_URL = 'http://localhost:8080/admin/realms/'
REALM_NAME = 'firstRealm'
CLIENT_ID = 'oidc_flaskapp'
CLIENT_SECRET = 'VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1'
CALLBACK_URL = 'http://localhost:5000/callback'

@app.route('/', methods=["GET"])
def index():
    keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER_URL,
                                     client_id=CLIENT_ID,
                                     realm_name=REALM_NAME,
                                     client_secret_key=CLIENT_SECRET)

    auth_url = keycloak_openid.auth_url(redirect_uri=CALLBACK_URL,
                                        scope="email",
                                        state="your_state_info")
    return redirect(auth_url)


@app.route('/callback', methods=["GET"])
def callback():
    code = request.args.get('code')
    keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER_URL,
                                     client_id=CLIENT_ID,
                                     realm_name=REALM_NAME,
                                     client_secret_key=CLIENT_SECRET)

    token = keycloak_openid.token(code, redirect_uri=CALLBACK_URL)
    keycloak_connection = KeycloakOpenIDConnection(server_url=KEYCLOAK_SERVER_URL,
                                                  client_id=CLIENT_ID,
                                                  realm_name=REALM_NAME,
                                                  client_secret_key=CLIENT_SECRET,
                                                  verify=True,
                                                  refresh_token=token['refresh_token'])

    keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

    username = "james"
    password = "James"
    email = "james@gmail.com"
    user = {
        "username": username,
        "enabled": True,
        "emailVerified": True,
        "email": email,
        "credentials": [
            {
                "type": "password",
                "value": password
            }
        ]
    }

    create_user_response = keycloak_admin.create_user(payload=user, exist_ok=False)
    return f"User created: {create_user_response['id']}"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, session, redirect,jsonify
import requests,json
from keycloak import KeycloakOpenID, KeycloakAdmin

app = Flask(__name__)
app.secret_key = 'SHYAM'  # Set a secret key for session management

# keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/admin/",
#                                  client_id="oidc_flaskapp",
#                                  realm_name="firstRealm",
#                                  client_secret_key="VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1")


# keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/admin/realms/firstRealm/users",
#                               username="shyam,",
#                               password="Shyam",
#                               realm_name="firstRealm",
#                               client_id="oidc_flaskapp",
#                               client_secret_key="VXhreHA0d4Zf3jKu5wcZ3cnaGAkcB1N1",
#                               verify=True)


# print('Retrieving Access token from Keycloak')



# @app.route('/')
# def test():
#     user = {
#     "username":"testuser",
#     "email":"testuser@example.com",
#     "credentials": [{"value": "password","type": "password"}],
#     "enabled":True
# }
#     create_user_response = keycloak_admin.create_user(payload= user,exist_ok=False)
#     return f"User created: {create_user_response['id']}"

@app.route('/')
def test():
    accessTokenUrl = "http://localhost:8080/realms/firstRealm/protocol/openid-connect/token"


    #update the admin credential for your keycloak instance
    username='shyam'
    password='Shyam'
    audience = 'oidc_flaskapp'
    payload='client_id=admin-cli&username='+username+'&password='+password+'&grant_type=password'+'&audience='+audience

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", accessTokenUrl, headers=headers, data=payload)

    access_token=json.loads(response.text)['access_token']
    print(access_token)
    addUserUrl = "http://localhost:8080/admin/realms/firstRealm/users"
    payload={
    "username":"usertest",
    "credentials": [{"value": "password","type": "password"}],
    "email":"usertest@gmail.com",
    "enabled":True
    }
    payload = jsonify(payload)
    print(payload)
    headers = {
        'Authorization': 'Bearer '+access_token+'',
        'Content-Type': 'application/json'
                }

    response = requests.request("POST", addUserUrl, headers=headers, data=payload)
    print(response)
    if (response.status_code==201):
        print(payload['username'] + ' user added successfully')
    elif (response.status_code==409):
        print(payload['username'] + ' already exist in the Keycloak')

if __name__ == "__main__":
    app.run(debug=True)

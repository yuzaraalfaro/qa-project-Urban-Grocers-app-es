# Crea un usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)




def user_token():
    response_token = post_new_user(data.user_body)
    return response_token.json()['authToken']


# Crea un kit
def post_new_kit(body):
    auth_token = user_token()
    kit_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=kit_headers)

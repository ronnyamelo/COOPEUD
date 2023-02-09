import requests
import os


class ClientCredentialsAuthorization():
    token = ''

    def __init__(self) -> None:
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.token_url = os.environ.get('TOKEN_ENDPOINT')
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def get_token(self):
        if self.token:
            return self.token
        
        self.token = self.get_new_token()
        return self.token

    def get_new_token(self):
        response = requests.post(url=self.token_url, 
                                headers=self.headers, 
                                data='grant_type=client_credentials', 
                                auth=(self.client_id, self.client_secret))

        if (response.ok):
            self.__set_token(response.json()['access_token'])
            return self.token

        return None

    def __set_token(self, token):
        self.token = token


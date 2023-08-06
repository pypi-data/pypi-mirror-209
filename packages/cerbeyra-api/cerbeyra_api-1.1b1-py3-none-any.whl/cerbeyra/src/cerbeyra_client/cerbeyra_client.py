from enum import Enum

import requests

from cerbeyra.exceptions import raise_exception_from_response, InvalidCredentialsException, ExpiredTokenException
from cerbeyra.src.cerbeyra_client.token import build_token_from_response, Token


class _ApiRequestMethod(Enum):
    GET = 'get'
    POST = 'post'


class CerbeyraClient:
    __login_uri = 'login'

    """
    A high-level representation of a session with the Cerbeyra platform. It provides an easy interface to simplify
    the authentication process and takes care of sending HTTP request and getting responses.
    """

    def __init__(self, username: str, password: str, endpoint: str, auto_reconnect=False, base_uri: str = '/api/'):
        """
        Creates a new CerbeyraClient.

        :param username: the email to be used for authentication.
        :param password: the password to be used for authentication.
        :param endpoint: the endpoint exposing Cerbeyra's API.
        :param auto_reconnect: a boolean indicating whether auto reconnection is needed after token expiration.
        :param base_uri: str
        """
        self.username = username
        self.password = password
        if endpoint.endswith('/'):
            endpoint = endpoint[:-1]
        endpoint += base_uri
        self.endpoint = endpoint
        self.auto_reconnect = auto_reconnect
        self.__token: Token | None = None

    def login(self):
        """
        Requests an access token. The token will be automatically used for API calls when needed.
        If credentials are invalid, then raises an InvalidCredentialsExceptions.
        """
        if self.__token:
            if self.__token.is_valid():
                return
            elif not self.auto_reconnect:
                raise ExpiredTokenException()
        uri = f"{self.endpoint}{self.__login_uri}"

        res = requests.post(uri, params=dict(email=self.username, password=self.password))
        if res.ok:
            self.__token = build_token_from_response(res.json())
            print(f'Successfully connected to {self.endpoint}')
            return
        raise InvalidCredentialsException()

    def get(self, api: str, params: dict = None, stream=False, client_id=None):
        """
        Sends an HTTP GET request to an API's endpoint. If params is specified, then the corresponding key-value
        pairs will be used to for constructing the URL's query string. Additionally, the stream parameter can be
        set to request the raw socket response. It is built on top of the requests library.

        :param client_id:
        :param api: the API endpoint.
        :param params: key-value pairs to be added at the URL's query string.
        :param stream: a boolean indicating whether request row socket response.
        :return: a request.models.Response object.
        """
        return self.request('get', api, params=params, stream=stream, client_id=client_id)

    def post(self, api: str, params: dict = None, stream=False, client_id=None):
        """
        Sends an HTTP POST request to an API's endpoint. If params is specified, then the corresponding key-value
        pairs will be used to for constructing the URL's query string. Additionally, the stream parameter can be
        set to request the raw socket response. It is built on top of the requests library.

        :param client_id:
        :param api: the API endpoint.
        :param params: key-value pairs to be added at the URL's query string.
        :param stream: a boolean indicating whether request row socket response.
        :return: a request.models.Response object.
        """
        return self.request('post', api, params=params, stream=stream, client_id=client_id)

    def request(self, method: str, api: str, params: dict = None, stream=False, client_id=None):
        assert _ApiRequestMethod(method)
        self.login()
        uri = self.__build_uri(api, client_id)
        headers = {'Authorization': self.__token.get_authorization_header()}
        response = requests.request(str(method), uri, headers=headers, params=params, stream=stream)
        if response.ok:
            return response

        return raise_exception_from_response(response)

    def __build_uri(self, api, client_id=None):
        uri = f"{self.endpoint}"
        if client_id is not None:
            uri += f"clients/{client_id}/"
        uri += api
        return uri

from cerbeyra.src.cerbeyra_client import CerbeyraClient


class Base:
    """
    Encloses a set of functions to make it easier getting resources through the Cerbeyra's APIs.
    It wraps CerbeyraClient.
    """

    def __init__(self, username: str = None, password: str = None, endpoint: str = None, auto_reconnect=False):
        """
        Builds a CerbeyraClient object to be used for negotiating with Cerbeyra.

        :param username: the email for authentication.
        :param password: the password for authentication.
        :param endpoint: the endpoint exposing Cerbeyra's API.
        :param auto_reconnect: a boolean indicating whether auto reconnection is needed after token expiration.
        """
        self._client = CerbeyraClient(username=username, password=password,
                                      endpoint=endpoint, auto_reconnect=auto_reconnect)

    def __enter__(self):
        """
        Makes the client callable with a context manager.

        :return: an already connected CerbeyraClient object.
        """
        self._client.login()
        return self

    def __exit__(self, *args):
        pass

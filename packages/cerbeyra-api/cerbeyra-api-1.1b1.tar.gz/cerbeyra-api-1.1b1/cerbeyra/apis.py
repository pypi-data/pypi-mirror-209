from cerbeyra.src import BaseApi


class CerbeyraApi(BaseApi):
    """
    Encloses a set of functions to make it easier getting resources through the Cerbeyra's APIs.
    It wraps CerbeyraClient.
    """

    def __init__(self, username: str, password: str, auto_reconnect=False):
        """
        Builds a CerbeyraClient object to be used for negotiating with Cerbeyra.

        :param username: the email for authentication.
        :param password: the password for authentication.
        :param auto_reconnect: a boolean indicating whether auto reconnection is needed after token expiration.
        """

        super().__init__(username, password, "https://areaclienti.cerbeyra.com", auto_reconnect=auto_reconnect)


class UbiqumApi(BaseApi):
    """
    Encloses a set of functions to make it easier getting resources through the Ubiqum's APIs.
    It wraps CerbeyraClient.
    """

    def __init__(self, username: str, password: str, auto_reconnect=False):
        """
        Builds a CerbeyraClient object to be used for negotiating with Ubiqum.

        :param username: the email for authentication.
        :param password: the password for authentication.
        :param auto_reconnect: a boolean indicating whether auto reconnection is needed after token expiration.
        """

        super().__init__(username, password, "https://areaclienti.ubiqum.ch", auto_reconnect=auto_reconnect)

    def get_ubiqum_index(self, client_id: int = None):
        """
        Gets a CerbeyraIndex object. If client_id is specified, then returns the cerbeyra index of specific clients.
        Otherwise, returns the cerbeyra index of the logged user.

        :param client_id: the unique identifier of a client.
        :return: a Cerbeyra Index object.
        """
        return super().get_cerbeyra_index(client_id=client_id)

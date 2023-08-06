from datetime import datetime, timedelta


class Token:
    """
    Defines a Token object.
    """

    def __init__(self, token: str, expire_time: float):
        self.token = token
        self.expire_on = datetime.now() + timedelta(seconds=expire_time)

    def get_authorization_header(self):
        """
        Builds the header which is needed to access Cerbeyra's resources.

        :return: a dictionary containing the header.
        """
        if self.token:
            return f'Bearer {self.token}'
        return None

    def is_valid(self):
        if self.token is None:
            return False
        if self.expire_on < datetime.now():
            self.token = None
            return False
        return True


def build_token_from_response(res_json) -> Token:
    return Token(res_json['access_token'], res_json['expires_in'])

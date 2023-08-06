class APIException(Exception):
    """
    Raised when something goes wrong during an API response handling.
    """
    message: str = "Generic HTTP Api Error"
    code: int = 500

    def __init__(self, status_code: int = None, message: str = None):
        if message:
            self.message = message
        if status_code:
            self.code = status_code

    def __str__(self):
        return f'The API request ended with an error (status code={str(self.code)}): {self.message})'


class InvalidCredentialsException(APIException):
    code = 401


class ExpiredTokenException(APIException):
    code = 401


def raise_exception_from_response(response):
    if response.status_code == UnauthenticatedApiException.code:
        raise UnauthenticatedApiException()
    if response.status_code == UnauthorizedApiException.code:
        raise UnauthorizedApiException()
    if response.status_code == NotFoundApiException.code:
        raise NotFoundApiException()
    if response.status_code == RateLimitExceededException.code:
        raise RateLimitExceededException()
    try:
        msg = response.json()['error']
        raise APIException(response.status_code, msg)
    except KeyError:
        pass
    raise APIException(response.status_code)


class UnauthenticatedApiException(APIException):
    code = 401


class UnauthorizedApiException(APIException):
    code = 403


class NotFoundApiException(APIException):
    code = 404


class RateLimitExceededException(APIException):
    code = 429

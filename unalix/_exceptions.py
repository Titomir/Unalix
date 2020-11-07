class InvalidURL(Exception):
    """URL is improperly formed or cannot be parsed."""
    def __init__(self, message: str, url: str) -> None:
        self.url = url
        super().__init__(message)

class InvalidScheme(Exception):
    """URL has a invalid or unknown scheme."""
    def __init__(self, message: str, url: str) -> None:
        self.url = url
        super().__init__(message)

class InvalidList(Exception):
    """It probably has no items or is not actually an object of the 'list' class."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidContentEncoding(Exception):
    """The 'Content-Encoding' header has an invalid/unknown value."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class TooManyRedirects(Exception):
    """The request exceeded maximum allowed redirects."""
    def __init__(self, message: str, url: str) -> None:
        self.url = url
        super().__init__(message)

class ConnectionError(Exception):
    """An error occurred during the request."""
    def __init__(self, message: str, reason: str, url: str) -> None:
        self.reason, self.url = reason, url
        super().__init__(message)

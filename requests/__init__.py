class RequestException(Exception):
    pass

class HTTPError(RequestException):
    pass

def get(*args, **kwargs):
    raise NotImplementedError('Network access disabled in test environment')

class exceptions:
    RequestException = RequestException
    HTTPError = HTTPError


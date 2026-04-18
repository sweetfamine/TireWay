class TireWayException(Exception):
    """
    Exceptionclass to handle all exceptions in the projekt
    """
    pass

class ConfigError(TireWayException):
    """Error in the config"""
    pass

class LoaderError(TireWayException):
    """Error while loading street data"""
    pass
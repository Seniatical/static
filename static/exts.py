from typing import (
    Callable, Any, List, Dict
)
from inspect import Parameter

class BaseException(Exception):
    r"""
    Base exception, all errors root from this exception

    Parameters
    ----------
    *args:`class:List[str]`:Arguments for the exception message
    **kwargs:`class:Dict[str, str]`:Addition keywords for forming messages etc.

    .. note::
        kwargs only uses one keyword which is `sep`. Defaults to a space and is used to join arguments from `*args`.
    """

    def __new__(cls, *args, **kwargs):
        message = kwargs.get('sep', ' ').join(args)

        cls.message = message
        return super().__new__(cls, message)


class ConversionError(BaseException):
    def __init__(self, message: str, cls: Callable[[Any], Any],
                 parameter: Parameter, argument: Any):

        self.message = message
        self.cls = cls
        self.parameter = parameter
        self.param_name = parameter.name
        self.argument = argument

        super(ConversionError, self).__init__(message, cls, parameter, argument)

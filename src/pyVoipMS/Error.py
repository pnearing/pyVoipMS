#!/usr/bin/env python3
"""
File: Error.py
Error classes.
"""

ERROR_MESSAGES: dict[int, str] = {
    0: "NO ERROR",
    1: "HTTP ERROR DURING REQUEST.",
    2: "CONNECTION ERROR DURING REQUEST.",
    3: "SERVER SENT INVALID JSON.",
    4: "VOIP.MS SENT ERROR.",
}


class Error(Exception):
    """
    Base voip.ms Exception.
    """
    def __init__(self, err_num: int, *args) -> None:
        self._err_num: int = err_num
        self._message: str = ERROR_MESSAGES.get(err_num, "UNDEFINED_ERROR_MESSAGE")
        Exception.__init__(self, *args)
        return

    @property
    def message(self) -> str:
        """
        The error message.
        :return: str: The error message.
        """
        return self._message

    @property
    def err_num(self) -> int:
        """
        The error number.
        :return: int: The error number.
        """
        return self._err_num


class RequestsError(Error):
    """
    Exception to throw if an error occurs during a 'requests' operation.
    """
    def __init__(self, err_num: int, requests_strerror: str, requests_errno: int, *args) -> None:
        """
        Initialize the 'requests' error.
        :param err_num: The internal error number, which corresponds to my error message.
        :param requests_strerror: The requests exception strerror property.
        :param requests_errno: The requests exception errno property.
        """
        Error.__init__(self, err_num, *args)
        self._requests_strerror: str = requests_strerror
        self._requests_errno: int = requests_errno
        return

    @property
    def strerror(self) -> str:
        """
        The requests exception strerror property.  Contains an error message.
        :return: str: The requests error message.
        """
        return self._requests_strerror

    @property
    def errno(self) -> int:
        """
        The requests exception errno property. Contains an error number.
        :return: The requests error number.
        """
        return self._requests_errno

#!/usr/bin/env python3
"""
File: Error.py
Error classes.
"""
from typing import Any

ERROR_MESSAGES: dict[int, str] = {
    0: "NO ERROR",
    1: "HTTP ERROR DURING REQUEST.",
    2: "CONNECTION ERROR DURING REQUEST.",
    3: "SERVER SENT INVALID JSON.",
    4: "VOIP.MS SENT AN ERROR.",
}


class Error(Exception):
    """
    Base voip.ms Exception.
    """
    def __init__(self, err_num: int, *args: list[Any]) -> None:
        """
        Initialize an error.
        :param err_num: int: The error number corresponding to an error message.
        :param *args: list[Any] Any additional arguments.
        """
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
    def __init__(self, err_num: int, requests_strerror: str, requests_errno: int, *args: list[Any]) -> None:
        """
        Initialize the 'requests' error.
        :param err_num: int: The internal error number, which corresponds to my error message.
        :param requests_strerror: str: The requests exception strerror property.IE: file not found.
        :param requests_errno: int: The requests exception errno property. IE: http 404.
        :param *args: list[Any]: Any additional arguments.
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
        :return: int: The requests error number.
        """
        return self._requests_errno


class VoipMSError(Error):
    """
    Exception for when voip.ms sends an error message.
    """
    def __init__(self, err_num: int, message: str, status: str, *args: list[Any]) -> None:
        """
        Initialize a Voip.ms error.
        :param err_num: int: The error number corresponding to my error message.
        :param message: str: The voip.ms response 'message' key. Contains a descriptive error message.
        :param status: str: The voip.ms response 'status' key. Contains a short error message.
        :param *args: list[Any]: Any additional arguments.
        """
        Error.__init__(self, err_num, *args)
        self._message: str = message
        self._status: str = status
        return

    @property
    def message(self) -> str:
        """
        The voip.ms response descriptive message.
        :return: str: The message.
        """
        return self._message

    @property
    def status(self) -> str:
        """
        The voip.ms response short error message.
        :return: str: The error message.
        """
        return self._status

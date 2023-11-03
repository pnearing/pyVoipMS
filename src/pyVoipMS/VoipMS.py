#!/usr/bin/env python3
from typing import Optional, Any
from .Error import Error
from .common import make_request
from .SubAccounts import SubAccounts


class VoipMS(object):
    """General voip.ms class."""
    def __init__(self, username: str, password: str) -> None:
        """
        Initialize the voip.ms object.
        :param username: str: The username to connect with, it's the email used to log in to the customer portal with.
        :param password: str: The password set in the API settings of the customer portal.
        """
        object.__init__(self)
        self._username: str = username
        self._password: str = password
        return

    def get_balance(self, advanced: bool = False) -> dict:
        params: Optional[dict[str, Any]] = None
        if advanced:
            params = {'advanced': advanced}
        response: dict[str, Any] = make_request(self._username, self._password, "getBalance", params)
        if response['status'] != 'success':
            raise Error(4, response['message'], response['status'])
        return response['balance']



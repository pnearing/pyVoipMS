#!/usr/bin/env python3
"""
File: common.py
Common Functions / Methods, Vars.
"""
from typing import Any, Optional
from requests import get, HTTPError, ConnectionError, JSONDecodeError, Response
from .Error import RequestsError

BASE_URL: str = 'https://voip.ms/api/v1/rest.php'
"""REST API base URL."""


def make_request(username: str,
                 password: str,
                 method: str,
                 params: Optional[dict[str, Any]] = None
                 ) -> dict[str, Any]:
    """
    Make the request from voip.ms.
    :param username: str: The API username.
    :param password: str: The API password.
    :param method: str: The method name.
    :param params: dict[str, Any]: Any parameters to the method.
    :return: dict[str, Any]: The json decoded object from voip.ms.
    """
    real_params: dict[str, Any] = {
        'api_username': username,
        'api_password': password,
        'method': method
    }
    if params is not None:
        real_params = real_params | params
    try:
        response: Response = get(url=BASE_URL, params=real_params)
        response.raise_for_status()
        reply: dict[str, Any] = response.json()
    except HTTPError as e:
        raise RequestsError(1, e.strerror, e.errno)
    except ConnectionError as e:
        raise RequestsError(2, e.strerror, e.errno)
    except JSONDecodeError as e:
        raise RequestsError(3, e.strerror, e.errno)
    return reply

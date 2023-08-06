#!/usr/bin/env python3
# Copyright (C) 2021-2023 All rights reserved.
# FILENAME:  core.py
# VERSION: 	 0.3.0
# CREATED: 	 2020-11-25 14:35
# AUTHOR: 	 Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
import re
from os import urandom
from hashlib import sha1
from typing import Optional
from fastapi.requests import Request
from fastapi.responses import Response
from starlette.datastructures import Headers
from itsdangerous import BadData, SignatureExpired, URLSafeTimedSerializer
from fastapi_csrf_protect.csrf_config import CsrfConfig
from fastapi_csrf_protect.exceptions import (
    InvalidHeaderError,
    MissingTokenError,
    TokenValidationError,
)


class CsrfProtect(CsrfConfig):
    def generate_csrf(self, secret_key: Optional[str] = None):
        """
        Generate a CSRF token.
        TODO: The token should be cached for a request, so multiple
        calls to this function will generate the same token.

        ---
        :param secret_key: (Optional) the secret key used when generating a new token for users
        :type secret_key: str
        """
        secret_key = secret_key or self._secret_key
        if secret_key is None:
            raise RuntimeError("A secret key is required to use CsrfProtect extension.")
        serializer = URLSafeTimedSerializer(secret_key, salt="fastapi-csrf-token")
        token = serializer.dumps(sha1(urandom(64)).hexdigest())
        return token

    def get_csrf_from_headers(self, headers: Headers) -> str:
        """
        Get token from the headers

        ---
        :param headers: Headers containing header with configured `header_name`
        :type headers: starlette.datastructures.Headers
        """
        header_name, header_type = self._header_name, self._header_type
        header_parts = None
        try:
            header_parts = headers[header_name].split()
        except KeyError:
            raise InvalidHeaderError(
                f'Bad headers. Expected "{header_name}" in headers'
            )
        token = None
        # Make sure the header is in a valid format that we are expecting, ie
        if not header_type:
            # <HeaderName>: <Token>
            if len(header_parts) != 1:
                raise InvalidHeaderError(
                    f'Bad {header_name} header. Expected value "<Token>"'
                )
            token = header_parts[0]
        else:
            # <HeaderName>: <HeaderType> <Token>
            if (
                not re.match(r"{}\s".format(header_type), headers[header_name])
                or len(header_parts) != 2
            ):
                raise InvalidHeaderError(
                    f'Bad {header_name} header. Expected value "{header_type} <Token>"'
                )
            token = header_parts[1]
        return token

    def set_csrf_cookie(
        self, csrf_token: Optional[str] = None, response: Optional[Response] = None
    ) -> None:
        """
        Sets Csrf Protection token to the response cookies

        ---
        :param csrf_token: (Optional) pre-determined token data
        :type csrf_token: str
        :param response: The FastAPI response object to sets the access cookies in.
        :type response: fastapi.responses.Response
        """
        csrf_token = csrf_token or self.generate_csrf(self._secret_key)
        if response and not isinstance(response, Response):
            raise TypeError("The response must be an object response FastAPI")
        response = response or self._response
        response.set_cookie(
            self._cookie_key,
            csrf_token,
            max_age=self._max_age,
            path=self._cookie_path,
            domain=self._cookie_domain,
            secure=self._cookie_secure,
            httponly=self._httponly,
            samesite=self._cookie_samesite,
        )

    def unset_csrf_cookie(self, response: Optional[Response] = None) -> None:
        """
        Remove Csrf Protection token from the response cookies

        ---
        :param response: (Optional) The FastAPI response object to delete the access cookies in.
        :type response: fastapi.responses.Response
        """
        if response and not isinstance(response, Response):
            raise TypeError("The response must be an object response FastAPI")
        response = response or self._response
        response.delete_cookie(
            self._cookie_key, path=self._cookie_path, domain=self._cookie_domain
        )

    def validate_csrf(
        self,
        request: Request,
        cookie_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        time_limit: Optional[int] = None,
    ):
        """
        Check if the given data is a valid CSRF token. This compares the given
        signed token to the one stored in the session.

        ---
        :param request: incoming Request instance
        :type request: fastapi.requests.Request
        :param cookie_key: (Optional) field name for the CSRF token field stored in cookies
            Default is set in CsrfConfig when `load_config` was called;
        :type cookie_key: str
        :param secret_key: (Optional) secret key used to decrypt the token
            Default is set in CsrfConfig when `load_config` was called;
        :type secret_key: str
        :param time_limit: (Optional) Number of seconds that the token is valid.
            Default is set in CsrfConfig when `load_config` was called;
        :type time_limit: int
        :raises TokenValidationError: Contains the reason that validation failed.
        """
        secret_key = secret_key or self._secret_key
        if secret_key is None:
            raise RuntimeError("A secret key is required to use CsrfProtect extension.")
        cookie_key = cookie_key or self._cookie_key
        cookie_token = request.cookies.get(cookie_key)
        if cookie_token is None:
            raise MissingTokenError(f"Missing Cookie: `{cookie_key}`.")
        time_limit = time_limit or self._max_age
        token: str = self.get_csrf_from_headers(request.headers)
        if token != cookie_token:
            raise TokenValidationError("The CSRF token pair submitted do not match.")
        serializer = URLSafeTimedSerializer(secret_key, salt="fastapi-csrf-token")
        try:
            serializer.loads(token, max_age=time_limit)
        except SignatureExpired:
            raise TokenValidationError("The CSRF token has expired.")
        except BadData:
            raise TokenValidationError("The CSRF token is invalid.")

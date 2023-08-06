import logging
import os
from enum import Enum
from typing import Dict

import requests
from requests.exceptions import HTTPError

from pyrasgo.version import __version__


def generate_headers(api_key: str) -> Dict:
    return {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "Rasgo-Client": "PyRasgo",
        "Rasgo-Client-Version": __version__,
    }


class InvalidApiKeyException(Exception):
    pass


class Environment(Enum):
    PRODUCTION = "api.rasgoml.com"
    STAGING = "staging-rasgo-proxy.herokuapp.com"
    LOCAL = "localhost"

    @classmethod
    def from_environment(cls):
        return cls(os.getenv("RASGO_DOMAIN", cls.PRODUCTION))

    @property
    def app_path(self):
        if self == self.PRODUCTION:
            return "https://app.rasgoml.com"
        if self == self.STAGING:
            return "https://staging.rasgoml.com"
        if self == self.LOCAL:
            return "http://localhost:9000"


class SessionMeta(type):
    _api_key = None
    _profile = None
    _dc = None
    _environment = None

    def __new__(mcs, name, bases, dct):
        new = super().__new__(mcs, name, bases, dct)
        logging.debug("Starting the session for user")
        new._environment = Environment.from_environment()
        new._api_key = mcs._api_key or None
        new._profile = mcs._profile or None
        new._dc = mcs._dc or None
        return new

    def __call__(cls, *args, **kwargs):
        if SessionMeta._api_key is None:
            api_key = kwargs.pop("api_key", None)
            if not api_key:
                raise InvalidApiKeyException("Must provide an API key to access the endpoint")
            SessionMeta._api_key = api_key
        if SessionMeta._environment is None:
            SessionMeta._environment = Environment.from_environment()
        if SessionMeta._profile is None or SessionMeta._dc is None:
            protocol = "http" if SessionMeta._environment.value == "localhost" else "https"
            profile_response = requests.get(
                f"{protocol}://{SessionMeta._environment.value}/v2/users/current-user",
                headers=generate_headers(SessionMeta._api_key),
                timeout=25,
            )
            dc_response = requests.get(
                f"{protocol}://{SessionMeta._environment.value}/v2/users/dw-credentials",
                headers=generate_headers(SessionMeta._api_key),
                timeout=25,
            )
            try:
                profile_response.raise_for_status()
                dc_response.raise_for_status()
            except HTTPError:
                raise InvalidApiKeyException(
                    f"The API key provided ({SessionMeta._api_key[:5]}...{SessionMeta._api_key[-5:]}) is not valid."
                )
            SessionMeta._profile = profile_response.json()
            SessionMeta._dc = dc_response.json()
        cls._api_key = SessionMeta._api_key
        cls._profile = SessionMeta._profile
        cls._dc = SessionMeta._dc
        cls._environment = SessionMeta._environment
        return type.__call__(cls, *args, **kwargs)


class Session(metaclass=SessionMeta):
    pass

    @property
    def api_key(self):
        return self._api_key

    @property
    def profile(self):
        return self._profile

# -*- coding: utf-8 -*-

import logging
import requests

from requests import Response

# Set up logger
logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

class HipolabsUniversitiesAPI:
    """ Main class for API wrapper. """
    def __init__(self, method, port=8080):
        self.method = method
        self.port = port if port is not None else 8080

    @staticmethod
    def _get_method(method, port):
        """ Selects the connection method, either remote or local. """
        if method == 'remote':
            return "http://universities.hipolabs.com/search"
        elif method == "local":
            return f"http://127.0.0.1:{port}/search"
        else:
            raise UniversitiesAPIError("Unknown method!")

    @staticmethod
    def _check_online(response: Response) -> None:
        """ Checks if API endpoint is online. """
        if response.status_code != 200:
            raise UniversitiesAPIError(response.text)

        logger.debug("Successful request: {}".format(response.status_code))

    @staticmethod
    def endpoints():
        """ Returns endpoints of universities API. """
        return ["name", "country"]

    def search(self, country=None, name=None) -> dict:
        """ This method searches by name and country. """

        base_url = self._get_method(self.method, self.port)

        if not country and not name:
            raise ValueError("Please provide valid university name or country.")
        elif not name:
            url = f"{base_url}?country={country.lower()}"
        elif not country:
            url = f"{base_url}?name={name.lower()}"
        else:
            url = f"{base_url}?name={name.lower()}&country={country.lower()}"

        response = requests.get(url=url)
        self._check_online(response)
        response = response.json()

        return response


class UniversitiesAPIError(Exception):
    """ Empty class used for raising exceptions. """
    pass

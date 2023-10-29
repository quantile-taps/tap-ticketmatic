"""REST client handling, including ticketmaticStream base class."""

import logging
from typing import Any, Dict, Optional

from requests import Response
from singer_sdk.authenticators import BasicAuthenticator
from singer_sdk.pagination import BaseOffsetPaginator
from singer_sdk.streams import RESTStream


class TicketmaticPaginator(BaseOffsetPaginator):
    """Custom ticketmatic paginator."""

    def has_more(self, response: Response) -> bool:
        """Checks if the Ticketmatic stream contains additional items."""
        response_json = response.json()
        results_key = "nbrofresults"

        # When ["data"] is empty, it does not return the "results_key".
        if results_key not in response_json.keys():
            logging.debug(
                f"The json response does not include the key {results_key}. Therefore, we don't paginate.")
            return False

        # If it contains data, check whether the current value is larger than the total number of data
        if self.current_value >= response_json[results_key]:
            logging.debug(
                f"Paginating: current value is {self.current_value} / the total number {response_json[results_key]}.")
            return False

        return True


class TicketmaticStream(RESTStream):
    """Ticketmatic stream class."""
    records_jsonpath = "$.data[*]"
    limit_per_request = 1000

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://apps.ticketmatic.com/api/1/{accountname}"

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Return a new authenticator object."""
        return BasicAuthenticator.create_for_stream(
            self,
            username=self.config["api_key"],
            password=self.config["api_secret"],
        )

    def get_url_params(
        self,
        context: Optional[dict],
        next_page_token: Optional[Any],
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        start_date = self.get_starting_timestamp(context)

        params = {
            "limit": self.limit_per_request,
            "output": "withlookup",
            "offset": next_page_token,
            "lastupdatesince": start_date,
        }

        return params

    def get_new_paginator(self) -> TicketmaticPaginator:
        """Paginator that focuses on fetching the based on the result the API returns."""
        return TicketmaticPaginator(
            start_value=0,
            page_size=self.limit_per_request,
        )

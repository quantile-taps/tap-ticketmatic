"""ticketmatic tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_ticketmatic.streams import Orders, Events, PriceTypes, SeatRanks

STREAM_TYPES = [
    Orders,
    Events,
    PriceTypes,
    SeatRanks,
]


class Tapticketmatic(Tap):
    """ticketmatic tap class."""
    name = "tap-ticketmatic"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "accountname",
            th.StringType,
            required=True,
        ),
        th.Property(
            "api_key",
            th.StringType,
            required=True,
        ),
        th.Property(
            "api_secret",
            th.StringType,
            required=True,
        ),
        th.Property(
            "start_date",
            th.StringType,
            default="2022-10-01",
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]

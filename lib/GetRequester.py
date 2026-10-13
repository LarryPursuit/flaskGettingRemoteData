import json
from typing import Any

import requests

# Seconds to wait for the server before giving up on the request.
REQUEST_TIMEOUT = 10


class GetRequester:
    """Sends HTTP GET requests to a URL and returns the raw or parsed response."""

    def __init__(self, url: str) -> None:
        # Store the endpoint so each method can reuse it.
        self.url = url

    def get_response_body(self) -> bytes:
        """Send a GET request to self.url and return the raw response body as bytes."""
        response = requests.get(self.url, timeout=REQUEST_TIMEOUT)
        # Raise an HTTPError for 4xx/5xx responses instead of returning an error page.
        response.raise_for_status()
        return response.content

    def load_json(self) -> Any:
        """Fetch the response body and parse it from JSON into Python objects."""
        return json.loads(self.get_response_body())

# Getting Remote Data Lab

A small, reusable Python class, `GetRequester`, that sends an HTTP GET request
to any URL and returns the response either as raw bytes or as parsed JSON.

## Description

`GetRequester` takes a URL when it's created and exposes two methods:

| Method | Returns | Purpose |
|--------|---------|---------|
| `get_response_body()` | `bytes` | Sends a GET request to the URL and returns the raw response body. Raises `requests.HTTPError` on a 4xx/5xx response and times out after 10 seconds. |
| `load_json()` | Python objects (`list` / `dict`) | Calls `get_response_body()` and parses the body with `json.loads`. |

The tests use this example endpoint:
`https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json`

## Installation

```bash
pipenv install
pipenv shell
```

## Usage

```python
from GetRequester import GetRequester

requester = GetRequester(
    "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
)

requester.get_response_body()
# b'[\n  {\n    "name": "Daniel",\n    "occupation": "LG Fridge Salesman"\n  }, ...'

requester.load_json()
# [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'}, {'name': 'Joe', ...}, ...]
```

Run it from the `lib/` directory, or with `lib` on your `PYTHONPATH`.

## Running Tests

```bash
pipenv run pytest
```

```
module get_response_body function returns response. .                    [ 50%]
module load_json function returns response. .                            [100%]

============================== 2 passed ===============================
```

<!-- Screenshot of passing tests: add the image to the repo and link it here, e.g. ![Passing tests](images/tests-passing.png) -->

## Project Structure

```
lib/
├── GetRequester.py              # GetRequester class
└── testing/
    ├── conftest.py              # pytest test-name formatting
    └── get_requester_test.py    # tests for both methods
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

See [LICENSE.md](LICENSE.md).

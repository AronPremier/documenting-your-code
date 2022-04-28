from typing import Union, Literal

import requests
from requests.exceptions import RequestException


def generate_random_fact(output_format: Literal["html", "json", "txt", "md"],
                         language: Literal["en", "de"]) -> Union[str, dict]:
    """
    Calls uselessfacts api and returns response
    :param output_format: str, should be one of: "html", "json", "txt", "md"
    :param language: str, should be "en" or "de"
    :return:
    """
    # sanity checks for inputs
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    response: requests.Response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    # response handler
    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact

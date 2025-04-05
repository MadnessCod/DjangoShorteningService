import hashlib
import random
import string

from typing import Any


def validate_input(entry: Any) -> None:
    """
    Checks if entry is string or not
    :param entry: Can be anything
    :type entry: Any
    :raises TypeError: if entry is not a string
    :return: None
    """
    if not isinstance(entry, str):
        raise TypeError("input must be an string ")


def random_number_plus_characters(url: str) -> str:
    """
    Creates a random 8 character from given string which first 4 are number
        and last 4 are letters (upper and lower)
    :param url: url string to create a random seed out of it
    :type url: str
    :raises TypeError: if url not a string
    :return: 8 character string which first 4 are numbers and last 4 are
        letters
    :rtype: str
    """
    try:
        validate_input(url)
    except TypeError:
        return "Invalid Input, url must be a string"

    hash_digest = hashlib.sha256(url.encode()).hexdigest()
    random.seed(int(hash_digest, 16))
    numbers = "".join(random.choices(string.digits, k=4))
    characters = "".join(random.choices(string.ascii_letters, k=4))
    return f"{numbers}{characters}"

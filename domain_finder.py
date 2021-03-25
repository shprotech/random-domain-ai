"""
Creator: shaharmelamed
Date: 3/25/21
Description: Find a non-existing domain.
"""
# ----- Imports ----- #

import random
import socket
import string

# ----- Functions ----- #


def _random_extension() -> str:
    """
    Get a random extension.

    :return: The random extension.
    """
    return random.choice(["com", "net", "il", "edu", "org"])


def find_domain() -> str:
    """
    Find a non-existing domain.

    :return: The non-existing domain.
    """
    found_domain = False
    while not found_domain:
        length = random.randint(1, 30)
        host = ''.join(random.choices(string.ascii_lowercase, k=length))
        domain = f"{host}.{_random_extension()}"

        try:
            socket.gethostbyname(domain)
        except socket.error:
            return domain

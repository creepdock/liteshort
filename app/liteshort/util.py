from getpass import getpass
from json import dumps
from sys import argv

import bcrypt
import requests


def check_url(key, url):
    out = requests.post(
        f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={key}",
        data=dumps(
            {
                "client": {"clientId": "liteshort"},
                "threatInfo": {
                    "threatTypes": [
                        "MALWARE",
                        "SOCIAL_ENGINEERING",
                        "UNWANTED_SOFTWARE",
                        "POTENTIALLY_HARMFUL_APPLICATION",
                    ],
                    "platformTypes": ["ANY_PLATFORM"],
                    "threatEntryTypes": ["URL"],
                    "threatEntries": [
                        {"url": url},
                    ],
                },
            }
        ),
    )
    return bool(out.json())


def hash_passwd():
    salt = bcrypt.gensalt()
    try:
        unhashed = getpass("Type password to hash: ")
        unhashed2 = getpass("Confirm: ")
    except (KeyboardInterrupt, EOFError):
        pass

    if unhashed != unhashed2:
        print("Passwords don't match.")
        return None

    hashed = bcrypt.hashpw(unhashed.encode("utf-8"), salt)

    print("Password hash: " + hashed.decode("utf-8"))

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from getmac import get_mac_address
import requests
import os

DEFAULT_DIRECTORY = os.path.join(os.getenv("HOME"), "Sync-Papad")

SYNCTHING_FOLDER = os.getenv("SYNCTHING_FOLDER", DEFAULT_DIRECTORY)


def main():
    mac = get_mac_address()
    mac = mac.replace(":", "")

    resp = requests.get("http://localhost:5000/recordings/")
    with open("{}/{}.json".format(SYNCTHING_FOLDER, mac), "w") as f:
        f.write(resp.text)


if __name__ == '__main__':
    main()

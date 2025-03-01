#!/usr/bin/env python3
"""
  generate_token.py
  Generate token for jupyterlab install
"""
import IPython as IPython

if __name__ == "__main__":
    print("Generate a access token")
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-p",
        "--password", 
        dest="password",
        help="The password you want to use for authentication.",
        required=True)
    args = parser.parse_args()

    print("\nCopy this line into the .env file:\n")
    hash = IPython.lib.passwd(args.password)
    print("ACCESS_TOKEN=" + hash)
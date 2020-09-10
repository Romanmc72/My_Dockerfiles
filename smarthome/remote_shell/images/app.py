#!/usr/env/bin python3
"""
Connects via SSH to the desired client and runs the command passed in
"""
import os
import argparse

import paramiko


def main(command: str):
    username = os.getenv('USERNAME')
    hostname = os.getenv('HOSTNAME')
    password = os.getenv('PASSWORD')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname, username=username, password=password)
    try:
        stdin, stdout, stderr = client.exec_command(command)
        print("Output: {output_text}".format(output_text=stdout.read().decode()))
        print("Error: {error_text}".format(error_text=stderr.read().decode()))
    finally:
        client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Pass in a string representing the command you wish to execute on the remote machine")
    parser.add_argument('--cmd', dest='cmd', type=str, help="The string representation of the command you wish to execute via SSH.")
    args = parser.parse_args()
    main(args.cmd)

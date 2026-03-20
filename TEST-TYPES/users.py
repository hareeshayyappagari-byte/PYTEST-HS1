from typing import Optional


users = {}



def add_user(username: str, password: str):# to add user to users dict
    users[username] = password

def remove_user(username: str):
    users.pop(username)

def get_user(username: str):
    return users.get(username)
#!/usr/bin/python3
"""user class, inherits base"""


from models.base_model import BaseModel


class User(BaseModel):
    """a class named User template that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

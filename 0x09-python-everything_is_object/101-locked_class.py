#!/usr/bin/pyton3
"""
Creates a LockedClass class that prevents the user from dynamically
creating new instance attributes, except if the new instance
attribute is called first_name:
"""


class LockedClass:
    """Will only allow first name attribute"""
    __slots__ = ['first_name']

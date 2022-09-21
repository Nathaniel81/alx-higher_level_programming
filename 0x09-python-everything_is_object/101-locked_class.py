#!/usr/bin/python3
"""Documentation for a single class definition"""


class LockedClass:
    """Prevents the user from dynamically creating new instance attributes"""

    __slots__ = ['first_name']

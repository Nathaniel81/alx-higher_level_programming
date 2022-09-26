#!/usr/bin/python3
"""Definition for a square class"""


R = __import__('9-rectangle').Rectangle


class Square(R):
    """Represents a class square"""
    def __init__(self, size):
        """Initiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

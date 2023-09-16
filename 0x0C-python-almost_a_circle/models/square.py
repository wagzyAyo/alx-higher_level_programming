#!/usr/bin/python3
"""This module contains The square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square class"""
        super().__init__(size, x, y, id)
        self.size = size
        self.x = x
        self.y = y
        self.id = None

    def __str__(self):
        """string representation of class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}

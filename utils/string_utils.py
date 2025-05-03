"""
String utility functions. module provides helper functions for string operations, including password hashing text transformation
"""

import hashlib


def hash_password(password: str) -> str:
    """
    Hash password using SHA - 256 Args : password : Plain text password to hash Returns : str : Hexadecimal representation of hashed password
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def to_upper(s: str) -> str:
    """
    Convert string to uppercase. Args : s : String to convert Returns : str : Uppercase version of input
    """
    return s.upper()

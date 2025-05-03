"""
Authentication service module. This module provides functions for user registration authentication, including password hashing validation
"""

from repository.user_repo import get_user, save_user
from utils.string_utils import hash_password


def register_user(user_id: int, name: str, password: str, balance=0.0):
    """
    Register new user or update existing user. If user with specified ID already exists, balance is preserved. password is hashed before storing. Args : user _ id : Unique identifier for user name : User ' s name password : User ' s plain text password ( will be hashed ) balance : Initial account balance ( default : 0. 0 ) Returns : User : registered User object Raises : ValueError : If balance is
    """
    from model.user import User

    if balance < 0:
        raise ValueError("Balance cannot be negative")

    existing_user = get_user(user_id)
    if existing_user:
        # Preserve existing user's balance
        balance = existing_user.balance

    hashed = hash_password(password)
    user = User(id=user_id, name=name, balance=balance)
    user.hashed_password = hashed
    save_user(user)
    return user


def authenticate(user_id: int, password: str):
    """
    Authenticate user with ID password. Args : user _ id : User ' s ID password : User ' s plain text password Returns : bool : True if authentication succeeds, False
    """
    user = get_user(user_id)
    if not user:
        return False
    return user.hashed_password == hash_password(password)

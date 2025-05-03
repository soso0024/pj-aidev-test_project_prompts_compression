"""
User repository module. This module provides data access functions for storing retrieving User objects in in - memory data store
"""

from model.user import User

# In-memory store for user objects
_user_store = {}


def save_user(user: User):
    """
    Save a user to data store. Args : user : User object to save Returns : bool : True if operation was
    """
    _user_store[user.id] = user
    return True


def get_user(user_id: int) -> User:
    """
    Retrieve user from data store by ID. Args : user _ id : ID of user to retrieve Returns : User : User object if found, None
    """
    return _user_store.get(user_id)

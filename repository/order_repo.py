"""
Order repository module. This module provides data access functions for storing retrieving Order objects in in - memory data store
"""

from model.order import Order

# In-memory store for order objects
_order_store = []


def save_order(order: Order):
    """
    Save an order to data store. Args : order : Order object to save Returns : bool : True if operation was
    """
    _order_store.append(order)
    return True


def list_orders_for_user(user_id: int):
    """
    Retrieve all orders for specific user. Args : user _ id : ID of user to get orders for Returns : list : List of Order objects for specified
    """
    return [o for o in _order_store if o.user_id == user_id]

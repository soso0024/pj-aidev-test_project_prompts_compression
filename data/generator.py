"""
Data generation module. This module provides functions to generate sample users orders for testing demonstration purposes
"""

import random
from model.user import User
from model.order import Order


def generate_users(n):
    """
    Generate list of sample users with random balances Args : n : Number of users to generate Returns : list : list of User objects with sequential IDs random balances Raises : ValueError : If n is
    """
    if n < 0:
        raise ValueError("Number of users must be positive")

    users = []
    for i in range(1, n + 1):
        users.append(User(id=i, name=f"User{i}", balance=random.uniform(10, 100)))
    return users


def generate_orders(users, max_orders=3):
    """
    Generate sample orders for list of users. Each user have 1 to max _ orders orders created, with order amounts not exceed user ' s current balance. Args : users : List of User objects max _ orders : Maximum number of orders per user Returns : list : list of Order
    """
    orders = []
    print("\nGenerating orders...")
    for user in users:
        available_balance = user.balance
        for _ in range(random.randint(1, max_orders)):
            if available_balance <= 1:  # Skip if below minimum order amount
                print("Skipping order generation due to insufficient balance.")
                break
            amount = random.uniform(1, min(available_balance, user.balance))
            order = Order(user_id=user.id, amount=amount)
            orders.append(order)
            available_balance -= amount
    return orders

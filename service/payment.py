"""
Payment service module. module provides functions for handling payment transactions, including deducting amounts from user balances recording orders
"""

from repository.user_repo import get_user, save_user
from repository.order_repo import save_order
from model.order import Order


def make_payment(user_id: int, amount: float):
    """
    Process a payment for a user. This function : 1. Deducts specified amount from user ' s balance 2. Creates a new order record 3. Saves both updated user and new order Args : user _ id : ID of user making payment amount : Amount to deduct from user ' s balance Returns : float : user ' s new balance after payment Raises : ValueError : If user is not found, has insufficient balance, or if payment amount is not
    """
    if amount <= 0:
        raise ValueError("Payment amount must be positive")

    user = get_user(user_id)
    if not user:
        raise ValueError("User not found")
    new_balance = user.debit(amount)
    order = Order(user_id=user_id, amount=amount)
    save_order(order)
    save_user(user)
    return new_balance

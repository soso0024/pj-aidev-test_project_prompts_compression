"""
Order model module. This module defines Order class represents financial transactions made by users in the system
"""

from datetime import datetime


class Order:
    """
    Order model representing a financial transaction. order is created when a user makes a payment and includes user ID, payment amount, and timestamp of transaction
    """

    def __init__(self, user_id: int, amount: float):
        """
        Initialize a new order. Args : user _ id : ID of user making payment amount : Amount of the
        """
        self.user_id = user_id
        self.amount = amount
        self.timestamp = datetime.utcnow()

    def summary(self):
        """
        Generate human - readable summary of order. Returns : str : summary string with user ID, amount, and timestamp
        """
        return f"Order for user {self.user_id}: ${self.amount:.2f} at {self.timestamp.isoformat()}"

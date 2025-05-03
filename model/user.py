"""
User model module. This module defines User class represents user accounts in system. Each user has an ID, name, and balance for financial transactions
"""


class User:
    """
    User model representing a customer account. A user has unique ID, name, and balance can be debited or credited for financial transactions
    """

    def __init__(self, id: int, name: str, balance: float):
        """
        Initialize new user. Args : id : Unique identifier for user name : User ' s name balance : Initial account
        """
        self.id = id
        self.name = name
        self.balance = balance

    def debit(self, amount: float):
        """
        Deduct an amount from user ' s balance. Args : amount : Amount to deduct Returns : float : new balance Raises : ValueError : If amount exceeds user ' s balance or is
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def credit(self, amount: float):
        """
        Add an amount to user ' s balance. Args : amount : Amount to add Returns : float : new balance Raises : ValueError : If amount is
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount
        return self.balance

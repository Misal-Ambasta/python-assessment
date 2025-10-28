class InsufficientFundsError(BaseException):
    def __init__(self):
        super().__init__()
        self.error = "Balance is less than withdrawal"

class Bank():
    def __init__(self, balance: int):
        self.balance = balance

    def withdrawal(self, amount: int):
        if amount > self.balance:
            raise ValueError from InsufficientFundsError

        return self.balance - amount
    
        
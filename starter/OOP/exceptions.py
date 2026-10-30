class InsufficientFundsError(Exception):
   
    def __init__(self, amount, msg=f"insufficient Funds"):
        self.amount = amount
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.amount} -> {self.msg}"
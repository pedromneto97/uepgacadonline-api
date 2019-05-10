from models.loan import Loan


class Loans:
    def __init__(self, loans):
        self.loans = [
            Loan(*[field for field in loan]).__dict__
            for loan in loans
        ]

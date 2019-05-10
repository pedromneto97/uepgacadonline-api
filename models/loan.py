from dataclasses import dataclass

import datetime

@dataclass
class Loan:
    name: str
    title: str
    address: str
    limitDate: datetime.datetime
    currentRenewalsNumber: int
    maxRenewalNumber: int
    renew: int
    fine: str

    def __post_init__(self):
        if type(self.currentRenewalsNumber) is str:
            self.currentRenewalsNumber = int(self.currentRenewalsNumber)

        if type(self.maxRenewalNumber) is str:
            self.maxRenewalNumber = int(self.maxRenewalNumber)

        if type(self.renew) is str:
            self.renew = int(self.renew)

        self.limitDate = datetime.datetime.strptime(self.limitDate, '%d/%m/%Y')


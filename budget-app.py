class Category:
    def __init__(self, title:str):
        self.ledger = []
        self.title = title
    def __str__(self) -> str:
        retString = ""
        retString += self.title.center(30, "*") + "\n"
        for item in self.ledger:
            retString += f'{item["description"][:23]:23}' + f'{item["amount"]:>7.2f}' + "\n"
        retString += f'Total: {self.get_balance():.2f}'
        return retString

    def deposit(self, amount:float ,description: str = ""):
        self.ledger.append({"amount": amount, "description": description})
    def withdraw(self, amount:float, description: str = ""):
        if not self.check_funds(amount):
            return False  
        self.ledger.append({"amount": -amount, "description": description})
        return True
    def get_balance(self) -> float:
        return sum(item["amount"] for item in self.ledger)
    def transfer(self, amount:float, category):
        if self.withdraw(amount, f'Transfer to {category.title}'):
            category.deposit(amount, f'Transfer from {self.title}')
            return True
        return False
    def getWithdrawal(self) -> float:
        return sum(item['amount'] for item in self.ledger if item['amount'] < 0)
    def check_funds(self, amount:float) -> bool:
        return self.get_balance() >= amount


def create_spend_chart(categories):
    retString = "Percentage spent by category\n"
    # values = list(item.get_balance() for item in categories)
    # total = sum(values)
    for i in range(100, -1, -10):
        retString += f'{i:3}|'
        for item in categories:
            if (item.getWithdrawal()/sum(list(cat.getWithdrawal() for cat in categories)))*100 > i:
                retString += " o "
            else:
                retString += "   "
        retString += " \n"
    retString += "".rjust(4) + "".ljust(len(categories)*3, "-") + "-\n"

    for i in range(max(len(item.title) for item in categories)):
        retString += f'    '
        for item in categories:
            try:
                retString += f' {item.title[i]} '
            except IndexError:
                retString += '   '
        if i == max(len(item.title) for item in categories)-1:
            retString += " "
            continue
        retString += ' \n'
    return retString

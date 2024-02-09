from multiprocessing import Value


class Category:
    def __init__(self, cat_name:str):
        self.cat_name = cat_name
        self.descriptions = {}
    def __str__(self):
        retString = ""
        retString += f'{self.cat_name:*^30}\n'
        for key in self.descriptions.keys():
            retString += f'{key[:23]:<23s}{self.descriptions[key]:7.2f}\n'
        retString += f'Total: {sum(self.descriptions.values()):7.2f}'
        return retString
    def deposit(self, amount:float, description:str):
        self.descriptions[description] = amount
    def withdraw(self, amount:float, description:str):
        if not self.check_funds(-amount):
            return False
        self.descriptions[description] = -amount
        return True
    def get_balance(self):
        return sum(self.descriptions.values())
    def transfer(self, amount:float, budget_name):
        if self.withdraw(amount,f'Transfer to {budget_name.cat_name}'):
            budget_name.deposit(amount, f'Transfer from {self.cat_name}')
            return True
        return False
    def check_funds(self, amount:float):
        return 0 < sum(self.descriptions.values()) + amount


def create_spend_chart(categories):
    retString = ""
    retString += "Percentage spent by category\n"
    total = sum(category.get_balance() for category in categories)
    print(total)
    return retString



food = Category("Food")
food.deposit(1000, "Initial Deposit")
food.withdraw(200, "Chicken")
orange_juice = Category("Orange Juice")
food.transfer(200,orange_juice)
print(food)

create_spend_chart([food, orange_juice])

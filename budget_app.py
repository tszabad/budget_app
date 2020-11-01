class Category:
    def __init__(self, name):
      self.name = name
      self.ledger = []
      self.budget = 0

    def deposit(self, amount, description = ""):
        self.budget += amount
        self.ledger.append({"amount": amount, "description": description})
        return True

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            self.budget -= amount
            amount *= -1
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount,f"Transfer to {category.name}" )
            category.deposit(amount, f"fTransfer from {self.name}")
            return False
        else:
            return True
        
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def get_balance(self):
        total = self.budget
        return total
    
    def __str__(self):
        tilte = "*"*(30-len(category.name))/2 + category.name + "*"*(30-len(category.name))/2



        *************Food*************
        deposit        1000.00
        groceries               -10.15
        restaurant and more foo -15.89
        Transfer to Clothing    -50.00
        Total: 923.96

def create_spend_chart(categories):
  pass
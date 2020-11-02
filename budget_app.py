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
        title_num = len(self.name)
        padding = int( (30 - title_num) / 2 )
        title = ("*"*padding )+ self.name + ("*"*padding)
        lines= ""
        for i in self.ledger:
            desc = i["description"][:23]
            am = float(i["amount"])
            am = format(am, '.2f')
            lines += str(desc) + str(am).rjust(30-len(desc)) + "\n"


        return title + "\n" + lines + "Total: "+ str(self.get_balance())



def create_spend_chart(categories):
  pass
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
        success = self.withdraw(amount,f"Transfer to {category.name}" )
        if success:
          category.deposit(amount, f"Transfer from {self.name}")
          return success
        else:
            return success
            
        
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
    title = "Percentage spent by category"
    x= len(categories)
    y = 100
    percentages = []
    total_spent = 0
    for i in categories: 
        total_spent += i.get_balance()
    for i in categories: 
            percent = i.get_balance() / total_spent
            percentages.append( int((percent) * 100))
        
    output = ""
    while y >= 0:
        output += "\n"
        output +=  str(y) + "| " if y == 100 else " " + str(y) + "| " if y < 100 and y > 0 else "  0| "
        i = 0
        while i < x:
            if percentages[i] >= y:  
                output += "o  "
            else: output += " "*3
            i += 1
        y -= 10  

    output += "\n" + " "*4 + "-" + "-"*x*3

    
    max_name_length = 0
    for i in categories: 
        if len(i.name) > max_name_length: 
            max_name_length = len(i.name) 
        
    z = 0
    while z < max_name_length: 
        output += "\n" + " "*5
        for i in categories:
            try: output += i.name[z] + " "*2
            except: output += " "*3

        z += 1

    return title + output
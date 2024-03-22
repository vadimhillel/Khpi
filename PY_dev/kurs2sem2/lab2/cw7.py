class User(object):
    def __init__(self, name: str, balance: int, checking_account: bool) -> None:
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    @staticmethod
    def validator(other, amount) -> None | ValueError:
        if not other.checking_account | other.balance - amount > 0:
            raise ValueError("{}'s checking account is disabled.".format(other.name))
        
    def withdraw(self, amount: int) -> str:
        User.validator(self, amount)
        self.balance -= amount
        return "{} has {}.".format(self.name, self.balance)
    
    def check(self, other, amount: int) -> str:
        User.validator(other, amount)
        self.balance += amount
        other.balance -= amount
        return "{} has {} and {} has {}.".format(self.name, self.balance, other.name, other.balance)
    
    def add_cash(self, amount: int) -> str:
        self.balance += amount
        return "{} has {}.". format(self.name, self.balance)
    
Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

print(Jeff.withdraw(2)) # Returns 'Jeff has 68.'

print(Joe.check(Jeff, 50)) # Returns 'Joe has 120 and Jeff has 18.'

print(Jeff.check(Joe, 80)) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

print(Jeff.check(Joe, 80)) # Returns 'Jeff has 98 and Joe has 40'

# print(Joe.check(Jeff, 100)) # Raises a ValueError

print(Jeff.add_cash(20.00)) # Returns 'Jeff has 118.'
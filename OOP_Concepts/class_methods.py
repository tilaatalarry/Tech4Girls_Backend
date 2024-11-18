class BankAccount:
    bank_name = "Tech4Girls Bank"
    
    def __init__(self, account_holder):
        """Initialize account holder and balance."""
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct money from the account if sufficient balance exists."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn. New balance: {self.balance}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    @staticmethod
    def bank_policy():
        """Print a generic bank policy message."""
        print("Welcome to Tech4Girls Bank. We value our customers!")

    @classmethod
    def get_bank_name(cls):
        """Return the bank name."""
        return cls.bank_name

account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

# Calling the static method to print bank policy
BankAccount.bank_policy()

# Calling the class method to get the bank name
print("Bank Name:", BankAccount.get_bank_name())

account1.deposit(900) 
account1.withdraw(600)  
account1.withdraw(400)  

account2.deposit(1300)  
account2.withdraw(800)   
account2.withdraw(700)  

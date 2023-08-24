from Bank import Bank

class User(Bank):
    __total_balance = 0

    def __init__(self, account_number, name, email, password) -> None:
        self.account_number = account_number
        self.name = name
        self.email = email
        self.__balance = 0
        self.__password = password
        
    ## User can create account
    def create_account(self, account_number, name, email, password):
        if account_number in Bank.accounts:
            print("This account number already exists. Please choose a different one.")
        else:
            account = User(account_number, name, email, password)
            Bank.accounts[account_number] = account
            print(f'{self.name} Account created successfully.')

    ## User can deposit
    def deposit(self, amount):
            if amount >= 500:
                Bank.accounts[self.account_number].__balance += amount
                User.__total_balance += amount
                Bank.total_balance = User.__total_balance
                Bank.add_transaction(Bank, 'Deposit', self.account_number, self.name, amount)
                print('Deposit successful.')
            else:
                print('Insufficient amount. You can deposit at least 500 or more.')

    ## User can withdraw
    def withdraw(self, amount):
        if Bank.total_balance <= 0:
            print('Bank is Bankrupt!')
        else:
            if Bank.accounts[self.account_number].__balance > 0:
                Bank.accounts[self.account_number].__balance -= amount
                User.__total_balance -= amount
                Bank.__total_balance = User.__total_balance
                Bank.add_transaction(Bank, 'Withdrawal', self.account_number, self.name, -amount)
                print('Withdrawal successful.')
            else:
                print('Oops! Insufficient amount for withdrawal.')

    ## User can transfer money
    def transfer(self, recipient, amount):
        if recipient != self and amount > 0 and amount <= Bank.accounts[self.account_number].__balance:
            Bank.accounts[recipient.account_number].__balance += amount
            Bank.accounts[self.account_number].__balance -= amount
            Bank.add_transaction(Bank, 'Transfer to', recipient.account_number, recipient.name, amount)
            Bank.add_transaction(Bank, 'Transfer from', self.account_number, self.name, amount)
            print('Transfer Successful.')
        else:
            print('Invalid Transfer.')

    ## User can take loan if admin not disabled loan feature
    def take_loan(self, amount):
        if Bank.is_loan_enabled:
            if amount <= 2 * Bank.accounts[self.account_number].__balance:
                Bank.accounts[self.account_number].__balance += amount
                Bank.add_transaction(Bank, 'Loan', self.account_number, self.name, amount)
                print(f'{self.name}\'s Loan Successfully taken')
                User.__total_balance -= amount
                Bank.__total_balance = User.__total_balance
                Bank.total_loan += amount
            else:
                print('You can not take loan this amount')
        else:
            print('Loan feature is disabled')

    ## User can check balance
    def check_balance(self):
        print(f'{Bank.accounts[self.account_number].name} Balance: {Bank.accounts[self.account_number].__balance}')

    ## User can check transaction history
    def check_transaction_history(self):
        print(f'-----------{self.name}\'s Transaction History--------')
        for transaction in Bank.transaction_history:
            for key, value in transaction.items():
                if value == self.account_number:
                    print(transaction)
        


from Bank import Bank

class Admin(Bank):
    def __init__(self, account_number, name, email, password) -> None:
        self.name = name
        self.account_number = account_number
        self.name = name
        self.email = email
        self.password = password

    ## Admin can create account
    def create_account(self, name, account_number, email, password):
        if account_number in Bank.admin_accounts:
            print("This account number already exists. Please choose a different one.")
        else:
            account = Admin(account_number, name, email, password)
            Bank.admin_accounts[account_number] = account
            print(f'{self.name} Account created successfully.')
        
    ## Admin can check total balance of bank
    def check_total_balance(self):
        print(f'Total balance in the bank: {Bank.total_balance}')

    ## Admin can check all transaction
    def check_transaction(self):
        print('-------------All Transaction-----------------')
        for transaction in Bank.transaction_history:
                print(transaction)

    ## Admin can on or off loan feature
    def toggle_loan_feature(self, value):
        Bank.is_loan_enabled = value

    ## Admin can check total loan taken
    def check_total_loan(self):
        print(f'Total loan taken: {Bank.total_loan}')


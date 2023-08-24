class Bank:
    __total_balance = 0
    accounts = {}
    admin_accounts = {}
    is_loan_enabled = True
    transaction_history = []
    total_loan = 0
    
    @property
    def total_balance(cls):
        return cls.__total_balance
    
    @total_balance.setter
    def total_balance(cls, amount):
        cls.__total_balance = amount

    def add_transaction(cls, description, account_number, name, amount):
        transaction = {
            'Description': description,
            'Account Number': account_number,
            'name': name,
            'Amount': amount
        }
        cls.accounts[account_number].transaction_history.append(transaction)

    

        
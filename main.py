from Admin import Admin
from User import User

def main():
    nazrul = User('1111', 'nazrul', 'nazrul@gmail.com', '4321') # User
    nazrul.create_account('1111', 'nazrul', 'nazrul@gmail.com', '4321') # User
    nazrul.deposit(5000)
    nazrul.check_balance() # User

    rahim = User('1112', 'rahim', 'rahim@gmail.com', '4322') # User
    rahim.create_account('1112', 'rahim', 'rahim@gmail.com', '4322') # User

    
    nazrul.deposit(4000) # User

    japor = Admin('1234', 'japor', 'japor@gmail.com', '5432') # Admin
    japor.create_account('1234', 'japor', 'japor@gmail.com', '5432') # Admin
    japor.check_total_balance() # Admin

    rahim.deposit(30000) # User
    rahim.check_balance() # User

    japor.check_total_balance() # Admin

    karim = Admin('1235', 'karim', 'karim@gmail.com', '5433') # Admin
    karim.create_account('1235', 'karim', 'karim@gmail.com', '5433') # Admin
    karim.check_total_balance() # Admin

    rahim.check_balance() # User

    rahim.withdraw(1000) # User
    rahim.check_balance() # User

    rahim.transfer(nazrul, 5000) # User
    nazrul.check_balance() # User

    karim.check_transaction() # Admin
    karim.check_total_balance() # Admin

    nazrul.take_loan(5000) # User
    nazrul.check_balance() # User

    karim.check_total_balance() # Admin

    rahim.check_balance() # User

    japor.toggle_loan_feature(False) # Admin

    nazrul.take_loan(5000) # User
    rahim.take_loan(5000) # User
    rahim.check_balance() # User
    nazrul.check_balance() # User

    japor.check_total_loan() # Admin
    japor.check_transaction() # Admin

    nazrul.check_transaction_history() # User
    rahim.check_transaction_history() # User

if __name__ == '__main__':
    main()

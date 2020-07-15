import uuid
class User():
    def __init__(self, first, last, dob, id):
        '''
        Create bank user.
        '''
        self.first = first
        self.last = last
        self.dob = dob
        self.id = id
        self.accounts = [] # Ids of the accounts (Account number)

    def create_account(self, amount):
        account_created = Account(self.id, amount)
        self.accounts.append(account_created.account_no) 

    

class Account():
    def __init__(self, user_id, amount):
        self.user_id = user_id
        self.amount = amount
        self.account_no = uuid.uuid1()

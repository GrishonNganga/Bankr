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
        self.accounts.append(account_created)

        return account_created

    def get_account(self):
        return self.accounts[0]

    def delete_account(self, account):
        for acc in self.accounts:
            if acc.account_no == account.account_no:
                self.accounts.remove(acc)
    

class Account():
    def __init__(self, user_id, amount):
        self.user_id = user_id
        self.amount = amount
        self.account_no = uuid.uuid1()

    def debit(self, amount):
        self.amount += amount

    def credit(self, amount):
        self.amount -= amount

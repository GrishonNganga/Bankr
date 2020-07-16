import unittest

from bank import User, Account

class TestUser(unittest.TestCase):

    def setUp(self):
        self.a_new_user = User('Grishon', 'Nganga', '20/20/1920', 31390865)

    def tearDown(self):
        self.a_new_user = None

    def test_user(self):
        a_new_user = User('Grishon', 'Nganga', '20/20/1920', 31390865)

        self.assertEqual(a_new_user.first, 'Grishon')
        self.assertEqual(a_new_user.last, 'Nganga')
        self.assertEqual(a_new_user.dob, '20/20/1920')
        self.assertEqual(a_new_user.id, 31390865)

    def test_account(self):
        self.user_account = Account(self.a_new_user.id, 2000)

        self.assertEqual(self.user_account.user_id, self.a_new_user.id)
        self.assertEqual(self.user_account.amount, 2000)
        

    def test_user_create_account(self):
        self.a_new_user.create_account(2000)

        self.a_new_user.accounts
        self.assertEqual(len(self.a_new_user.accounts), 1)

    def test_user_debit_account(self):
        self.a_new_user.create_account(2000)
        account = self.a_new_user.accounts[0]    

        account.debit(200)        
        
        self.assertEqual(self.a_new_user.accounts[0].amount, 2200)

    def test_user_credit_account(self):
        self.a_new_user.create_account(2000)

        self.a_new_user.accounts
        self.assertEqual(len(self.a_new_user.accounts), 1)

    def test_user_debit_account(self):
        self.a_new_user.create_account(2000)
        account = self.a_new_user.accounts[0]    

        account.credit(200)        
        
        self.assertEqual(self.a_new_user.accounts[0].amount, 1800)


    def test_delete_account(self):
        self.a_new_user.create_account(100)
        
        self.a_new_user.delete_account(self.a_new_user.accounts[0])

        self.assertEqual(len(self.a_new_user.accounts), 0)

if __name__ == '__main__':
    unittest.main()
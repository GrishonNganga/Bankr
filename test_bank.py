import unittest

class TestUser(unittest.TestCase):

    def setUp(self):
        print('We good')
        pass

    def tearDown(self):
        pass

    def test_user(self):
        pass

if __name__ == '__main__':
    unittest.main()
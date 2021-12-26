import unittest
from database.user_repository import UserRepository
from database.database_init import initialize_database
from database.database_connection import get_database_connection

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_repository = UserRepository()
    
    def test_get_topfive(self):
        topfive = self.user_repository.get_topfive()

        self.assertEqual(topfive, [{'username': 'Sampsa', 'score': 6}, {'username': 'Jukka', 'score': 4},
            {'username': 'Jorkki', 'score': 2}, {'username': 'Pertsa', 'score': 2}, {'username': 'Seppo', 'score': 1}])

    def test_check_score(self):
        topfive = self.user_repository.check_score("Jeppe", 10)

        self.assertEqual(topfive, True)
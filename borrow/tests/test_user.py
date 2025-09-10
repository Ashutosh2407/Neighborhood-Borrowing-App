from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username = "User1", password= "abc123")

    def test_instance_creation(self):
        self.assertEqual(self.user.username, "User1")
        self.assertTrue(self.user.check_password("abc123"))

    def test_instance_tostring(self):
        self.assertEqual(str(self.user), "User1")

    
from django.test import TestCase


# Create your tests here.
from chat_backend.chats.consumers import User


class UserTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            name="Alexander",
        )
        user.save()
        self.assertEqual("Alexander", user.name)
from django.contrib.auth import get_user_model

User = get_user_model()


def get_users_count():
    return User.objects.all()

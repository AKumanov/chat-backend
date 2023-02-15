from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    """
    Default custom user model for Chat Backend Project
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=260)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """
        Get URL for user's detail view.
        :return:
            str: URL for user detail.
        """
        return reverse("users: detail", kwargs={"username": self.username})

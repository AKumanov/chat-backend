from django.db import models
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()


class Conversation(models.Model):
    __NAME_MAX_LENGTH = 128
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=__NAME_MAX_LENGTH
    )
    online = models.ManyToManyField(
        to=User,
        blank=True
    )

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.remove(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return "{} ({})".format(self.name, self.get_online_count())


class Message(models.Model):
    __CONTENT_MAX_LENGTH = 512
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages_from_me"
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages_to_me"
    )
    content = models.CharField(
        max_length=__CONTENT_MAX_LENGTH
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    read = models.BooleanField(
        default=False
    )

    def __str__(self):
        return "{} to {}: {} [{}]".format(self.from_user.username, self.to_user.username, self.content, self.timestamp)

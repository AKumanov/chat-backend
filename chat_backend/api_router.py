from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from chat_backend.chats.views import UserViewSet
from chat_backend.chats.api.views import ConversationViewSet, MessageViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("conversations", ConversationViewSet)
router.register("messages", MessageViewSet)
urlpatterns = router.urls

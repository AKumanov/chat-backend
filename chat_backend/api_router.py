from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from chat_backend.chats.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("conversations", ConversationViewSet)
router.register("users", UserViewSet)

urlpatterns = router.urls

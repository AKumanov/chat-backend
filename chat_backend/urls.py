from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView


class CustomObtainAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-token/', CustomObtainAuthTokenView.as_view(), name='auth_login'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("users/", include("chat_backend.users.urls", namespace="users")),
]

urlpatterns += [
    path("api/", include("chat_backend.api_router")),
]

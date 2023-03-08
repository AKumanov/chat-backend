from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Snippets API',
        default_version='V1',
        description='Test description',
        terms_of_service='https://google.com/policies/terms/',
        contact=openapi.Contact(email='contact@snippets.local'),
        license=openapi.License(name='BSD Licence')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


class CustomObtainAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})


urlpatterns = [
    path(r'swagger^(?P<format>\.json|\yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('auth-token/', CustomObtainAuthTokenView.as_view(), name='auth_login'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("users/", include("chat_backend.users.urls", namespace="users")),
    path('', include('chat_backend.chats.urls')),
]

urlpatterns += [
    path("api/", include("chat_backend.api_router")),
]

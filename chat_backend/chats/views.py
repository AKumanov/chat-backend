from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, RedirectView
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from chat_backend.chats.serializers import UserSerializer

User = get_user_model()


# Create your views here.
class UserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def all(self, request):
        serializer = UserSerializer(
            User.objects.all(), many=True, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

from django.urls import path

from chat_backend.chats.views import UserSetView

LIST_VIEW_METHODS = {
    'get': 'list',
    'post': 'create',
}

DETAIL_VIEW_DATA = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
}

users_list = UserSetView.as_view({**LIST_VIEW_METHODS})
users_detail = UserSetView.as_view({**DETAIL_VIEW_DATA})

urlpatterns = [
    path('new/users/', users_list, name='users-list'),
    path('new/users/<int:pk>', users_detail, name='users-detail'),
]

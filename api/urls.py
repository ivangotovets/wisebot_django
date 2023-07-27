from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import MessageViewset, RandomMessageView


router = DefaultRouter()
router.register('messages', MessageViewset, basename='messages')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/random/', RandomMessageView.as_view())
]

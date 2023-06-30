from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import MessageViewset


router = DefaultRouter()
router.register('messages', MessageViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
]

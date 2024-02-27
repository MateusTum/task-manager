from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

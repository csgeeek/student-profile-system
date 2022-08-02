from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import StudentModelViewSet

router = DefaultRouter()

router.register('', StudentModelViewSet)

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('v2/', include(router.urls)),
]
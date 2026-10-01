from django.urls import path, include
from .views import BlogViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comments', CommentViewSet, basename='comments')
router.register('', BlogViewSet, basename='blogs')


urlpatterns = [
    path('', include(router.urls)),
]

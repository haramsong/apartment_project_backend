from django.urls import include, path
from rest_framework import routers
from . import views #views.py import

router = routers.DefaultRouter() #DefaultRouter를 설정
router.register('Attachs', views.AttachsViewSet)
router.register('BoardContents', views.BoardContentsViewSet)
router.register('Danjis', views.DanjisViewSet)
router.register('UserGroups', views.UserGroupsViewSet)


urlpatterns = [
    path('', include(router.urls))
]
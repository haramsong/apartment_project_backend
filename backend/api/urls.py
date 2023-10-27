from django.urls import include, path
from rest_framework import routers

from .apps.Attachs import views as attachs_views
from .apps.BoardContents import views as board_contents_views
from .apps.Danjis import views as danjis_views
from .apps.UserGroups import views as user_groups_views


router = routers.DefaultRouter()    # Default Router를 설정
router.register('Attachs', attachs_views.AttachsViewSet)
router.register('BoardContents', board_contents_views.BoardContentsViewSet)
router.register('Danjis', danjis_views.DanjisViewSet)
router.register('UserGroups', user_groups_views.UserGroupsViewSet)


urlpatterns = [
    path('', include(router.urls))
]
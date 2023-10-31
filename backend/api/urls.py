from django.urls import include, path
from rest_framework import routers

# views
from .apps.Attachs import views as attachs_views
from .apps.BoardContents import views as board_contents_views
from .apps.Danjis import views as danjis_views
from .apps.UserGroups import views as user_groups_views
from .apps.Users import views as users_views


router = routers.DefaultRouter()    # Default Router를 설정

router.register('attachs', attachs_views.AttachsViewSet)
router.register('board_contents', board_contents_views.BoardContentsViewSet)
router.register('danjis', danjis_views.DanjisViewSet)
router.register('user_groups', user_groups_views.UserGroupsViewSet)
router.register('users', users_views.UsersViewSet)



urlpatterns = [
    path('', include(router.urls))
]

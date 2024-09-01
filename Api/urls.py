from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views.company_view import CompanyViewSet
from .views.project_view import ProjectViewSet
from .views.user_view import UserViewSet
from .views.user_story_view import UserStoryViewSet
from .views.ticket_view import TicketViewSet



router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'users', UserViewSet, basename='user')
router.register(r'user-stories', UserStoryViewSet, basename='userstory')
router.register(r'tickets', TicketViewSet, basename='ticket')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/<int:project_id>/user-stories/', UserStoryViewSet.as_view({'get': 'list'}), name='project_user_stories'),
    path('user-stories/<int:user_story_id>/tickets/', TicketViewSet.as_view({'get': 'list'}), name='user_stories_tickets'),
    path('', include(router.urls)),
    
]

"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from journal import views as post_views
from rest_framework import routers, viewsets
from users import views as account_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

##logout
# from users.views import LogoutView
# from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users.views import BlacklistTokenUpdateView

router = routers.DefaultRouter()
router.register(r'ownpost', post_views.OwnPostView, 'ownpost')
router.register(r'post', post_views.PostView, 'post')
# router.register(r'user', account_views.UserView, 'user')
# router.register(r'register', account_views.UserCreate, 'users')
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('journal.urls', namespace='journal')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register', account_views.UserCreate.as_view()),
    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
]

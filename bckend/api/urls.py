from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    # path('auth/', obtain_auth_token),
    # path('', views.api_home),
    path('signup/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
]

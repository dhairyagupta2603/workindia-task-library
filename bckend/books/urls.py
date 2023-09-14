from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('borrow/', views.BookBorrowAPIView.as_view()),
    path('create/', views.BookAddAPIView.as_view()),
    # path('auth/', obtain_auth_token),
    path('<int:pk>/availablity/', views.BookAvailiblityAPIView.as_view()),
    path('', views.BookSearchAPIView.as_view()),
]

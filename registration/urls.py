from django.urls import path
from .views import SignUp,LoginView
urlpatterns = [
    path('nuevo/',SignUp.as_view(), name='signup'),
    path('login/',LoginView.as_view(),name='login'),
]
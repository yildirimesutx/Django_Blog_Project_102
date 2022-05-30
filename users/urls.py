
from django.urls import path
from .views import home, register, test, user_logout

urlpatterns = [
    path('', home, name="home"),
    path('test', test, name="test"),
    path('logout', user_logout, name="logout"),
    path('register', register, name="register"),
]
from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path('add',views.add,name="result"),
    path('display',views.display,name="display"),
    path('home',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name='login')
]

from django.urls import path
from django.views.decorators.csrf import csrf_exempt


from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout_usr, name = 'logout'),
]
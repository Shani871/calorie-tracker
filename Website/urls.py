from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete_consume, name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update-goal/', views.update_goal, name='update_goal'),
    path('profile/', views.profile_view, name='profile'),
]

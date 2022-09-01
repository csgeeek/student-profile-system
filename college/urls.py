from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='college-head-home'),
    path('login/', views.loginPage, name='college-head-login'),
    path('logout/', views.logoutPage, name='college-head-logout'),
    path('add-student/', views.add_student, name='add-student'),
    path('update-student/<str:pk>/', views.update_student, name='update-student'),
    path('delete-student/<str:pk>/', views.delete_student, name='delete-student'),
]

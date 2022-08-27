from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='govt-official-home'),
    path('login/', views.loginPage, name='govt-official-login'),
    path('logout/', views.logoutPage, name='govt-official-logout'),
    path('register/', views.registerGovtOfficialPage, name='register-govt-official'),
    path('register-college-and-head/', views.registerCollegeAndHead, name='register-college-and-head'),
    path('view-students/<str:college_id>/', views.viewStudentsListByCollege, name='view-students'),
]


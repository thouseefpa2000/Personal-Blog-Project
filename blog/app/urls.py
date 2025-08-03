from . import views
from django.urls import path

urlpatterns = [
    path('',views.base,name='index'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('register',views.register_view,name='register'),
    path('myblog',views.myblog,name='myblog'),
    path('readblog',views.readblog,name='readblog'),
    path('pratice',views.pratice,name='pratice'),
    path('answer',views.answer,name='answer'),
    path('dashboard',views.dashboard,name='dashboard'),
    
    # search
    path('myblog/', views.myblog, name='myblog'),

    # crud 
    path('createblog',views.blogCreate,name='createblog'),
    path('deleteblog/<int:pk>/',views.deleteblog,name='deleteblog'),
    path('readblog/<int:pk>/',views.readblog,name='readblog'),
    path('updateblog/<int:pk>/',views.updateblog,name='updateblog'),
    
   
    path('createpratice/', views.createpratice, name='createpratice'),  # trailing slash is best practice
    path('deletepratice/<int:pk>/', views.deletepratice, name='deletepratice'),
    path('pratice/', views.pratice, name='pratice'),
    path('answer/<int:pk>/', views.answer, name='answer'),
    path('updatepratice/<int:pk>/', views.updatepratice, name='updatepratice'),


    
    
]

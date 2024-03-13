from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'),

]

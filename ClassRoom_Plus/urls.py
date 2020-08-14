"""ClassRoom_Plus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home, name='home'),

    path('signup/', views.signupuser, name='signupuser'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

    path('login/',views.loginuser, name='loginuser'),
    path('logout/',views.logoutuser, name='logoutuser'),
    path('profile/',views.profile, name='profile'),
    path('accounts/login/', views.loginuser, name='loginuser'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('v1/', include('UserApi.urls')),

    path('newsession/',views.new_session,name='new_session'),
    url(r'^session/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/[1-9][0-9]?$|^100/$',views.user_session, name='user_session'),
    path('joinsession/',views.joinsession, name='joinsession'),

    url(r'^makequiz/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/[1-9][0-9]?$|^100/$',views.makequiz, name='makequiz'),
    url(r'^quizresponse/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/[1-9][0-9]?$|^100/$',views.quizresponse, name='quizresponse'),
    url(r'^freeresponse/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/[1-9][0-9]?$|^100/$',views.freeresponse, name='freeresponse'),

    url(r'^icebreaker/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/[1-9][0-9]?$|^100/$',views.icebreaker, name='icebreaker')



]

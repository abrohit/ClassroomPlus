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

    path('dashboard/', views.dashboard, name='dashboard'),

    path('v1/', include('UserApi.urls'))
]

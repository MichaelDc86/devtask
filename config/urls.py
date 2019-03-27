"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from authapp.views import CustomPasswordResetView
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from authapp import views as views
from rest_auth.views import PasswordResetConfirmView
from rest_auth.serializers import PasswordResetSerializer
from rest_auth.urls import urlpatterns

urlpatterns = [

    path('dashboard/', admin.site.urls),

    re_path(r'^api/$', views.api_root),

    re_path(r'^project/', include('project.api.urls', namespace='project')),

    # re_path('^api/', include('rest_framework.urls', namespace='api')),

    re_path('^auth/', include('rest_auth.urls')),
    re_path('^auth/password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    re_path(r'^auth/password/reset/confirm/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    re_path('^api/', include('authapp.api.urls', namespace='api')),

    re_path(r'^auth/verify/social/', include("social_django.urls", namespace="social")),
    re_path(r'^social/', include('auth_social.urls', namespace='social_view')),
]

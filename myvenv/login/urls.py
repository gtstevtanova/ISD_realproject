from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView)


urlpatterns = [
    path('register/',views.register, name='register'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    path('profile/password/',PasswordResetView.as_view(), name='change-profile'),


]

'''Defines URL patterns for the deploy_app'''

from django.urls import path

from . import views

app_name = 'deploy_app2'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('manager/', dashboard_manager, name='dash-manager'),
    path('panitia/', dashboard_panitia, name='dash-panitia'),
    path('penonton/', dashboard_penonton, name='dash-penonton'),
]
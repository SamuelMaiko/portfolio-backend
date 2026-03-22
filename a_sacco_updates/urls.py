from django.urls import path
from .views import download_apk

app_name = 'a_sacco_updates'

urlpatterns = [
    # Uses version_name as the version param (can be string like '1.3.0').
    path('download/<str:version_name>/', download_apk, name='download_apk'),
]

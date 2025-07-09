from django.urls import path
from .views import ServicesView

urlpatterns = [
    path('', ServicesView.as_view(), name='services'),
]

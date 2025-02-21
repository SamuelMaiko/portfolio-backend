from django.urls import path
from .views import ReceiveEmailView

urlpatterns = [
    path('receive-email/', ReceiveEmailView.as_view(), name='receive-email'),
]

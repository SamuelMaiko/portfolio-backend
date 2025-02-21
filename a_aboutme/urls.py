from django.urls import path
from .views import AboutMeInfoView, AboutMeCardsView

urlpatterns = [
    path('info/', AboutMeInfoView.as_view(), name='aboutme-info'),
    path('cards/', AboutMeCardsView.as_view(), name='aboutme-cards'),
]

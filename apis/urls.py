from django.urls import path, include
from .views import PortfolioView

urlpatterns = [
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('contactme/', include('a_contactme.urls')),
]

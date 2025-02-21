from django.urls import path, include

urlpatterns = [
    path('profile/', include('a_profile.urls')),
    path('aboutme/', include('a_aboutme.urls')),
]

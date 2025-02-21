from django.urls import path, include

urlpatterns = [
    path('profile/', include('a_profile.urls')),
    path('aboutme/', include('a_aboutme.urls')),
    path('skill/', include('a_skills.urls')),
    path('projects/', include('a_projects.urls')),
    path('contactme/', include('a_contactme.urls')),
]

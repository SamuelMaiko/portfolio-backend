from django.urls import path
from a_projects.views import ProjectsListView

urlpatterns = [
    path('/', ProjectsListView.as_view(), name='projects-list'),
]

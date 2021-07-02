from django.urls import path
from rest_framework.generics import CreateAPIView
from .views import ProjectViewSet, ProjectRetrieveDestroyView

urlpatterns = [
    path('projects/', ProjectViewSet.as_view()),
    path('projects/<name>/',  ProjectRetrieveDestroyView.as_view())]
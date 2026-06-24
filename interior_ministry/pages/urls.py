from django.urls import path
from .views import dashboard_view, home_view, survey_view

urlpatterns = [
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('survey/', survey_view, name='survey')
]
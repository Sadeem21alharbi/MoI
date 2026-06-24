from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

def dashboard_view(request):
    return render(request, 'pages/dashboard.html')

def survey_view(request):
    return render(request, 'pages/survey.html')
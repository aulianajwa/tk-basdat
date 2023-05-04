from django.shortcuts import render

# Create your views here.
def dashboard_manager(response) : 
    return render(response, 'dash_manager.html')

def dashboard_panitia(response) : 
    return render(response, 'dash_panitia.html')

def dashboard_penonton(response) : 
    return render(response, 'dash_penonton.html')
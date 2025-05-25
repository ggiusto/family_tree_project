# family_tree_project/views.py

from django.shortcuts import render

def home_view(request):
    """
    Vista para renderizar la página de inicio del proyecto (index.html).
    """
    return render(request, 'index.html')

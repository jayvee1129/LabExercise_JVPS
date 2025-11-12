from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

from django.shortcuts import render

# Homepage view 
def homepage(request):
    return render(request, 'homepage.html')

# Login page view
def login(request):
    return render(request, 'login.html')

# About Us page view
def about(request):
    return render(request, 'about.html')

# Contact Us page view
def contact(request):
    return render(request, 'contact.html')


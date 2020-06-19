from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request,'index.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request, 'contact.html')

def portfoliopage(request):
    return render(request, 'portfolio.html')

def portfolio_details(request):
    return render(request, 'portfolio_details.html')

def services(request):
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')

def elements(request):
    return render(request, 'elements.html')

def main(request):
    return render(request, 'main.html')

def single_blog(request):
    return render(request, 'single-blog.html')
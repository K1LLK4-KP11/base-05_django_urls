from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.
def pages_req(request):   
    return render(request, 'pages/pages.html')  


def contact(request):   
    return render(request, 'pages/contact.html')  

def about(request):   
    return render(request, 'pages/about.html')  




def error_404(request, exception):
    return render(request, '404.html', status=404) 

def error_500(request):
    return render(request, '505.html', status=500)
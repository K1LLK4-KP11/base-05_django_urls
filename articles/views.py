from django.shortcuts import render

# Create your views here.
def articles_req(request):   
    return render(request, 'articles/articles.html')  


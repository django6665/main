from django.shortcuts import render

# Create your views here.
def home(request):
    content={
        "request":request,
        'dir_request':dir(request),
        }
    return render(request,"index.html",content)
def create(request):
    content={

        }
    return render(request,"create.html",content)
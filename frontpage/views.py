from django.shortcuts import render

# Create your views here.

def frontpage(request):
    return render(request, "frontpage/index.html")

def mentions(request):
    return render(request, "frontpage/mentions.html")
    
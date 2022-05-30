from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"cv/index.html")
def about(request):
    return render(request,"cv/about.html")
# def contact(request):
#     return render(request,"cv/contact.html")
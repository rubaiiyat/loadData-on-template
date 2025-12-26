from django.shortcuts import render

# Create your views here.
def meals(request):
    return render(request,'meals.html')

def about(request):
    return render(request,'about.html')
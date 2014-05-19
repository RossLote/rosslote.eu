from django.shortcuts import render

def index(request):
    return render(
        request,
        'rosslote/index.html'
    )

def about(request):
    return render(
        request,
        'rosslote/about.html'
    )

def cv(request):
    return render(
        request,
        'rosslote/cv.html'
    )


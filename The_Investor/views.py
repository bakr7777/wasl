from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def browse(request):
    return render(request, 'pages/browse.html')

def details(request):
    return render(request, 'pages/details.html')

def streams(request):
    return render(request, 'pages/streams.html')

def profile(request):
    return render(request, 'pages/profile.html')    
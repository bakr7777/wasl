from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')

def deals(request):
    return render(request, 'pages/deals.html')

def reservation(request):
    return render(request, 'pages/reservation.html')

def login(request):
    return render(request, 'pages/login.html')    

def signIn(request):
    return render(request, 'pages/signIn.html')

def vir(request):
    return render(request, 'pages/vir.html')

def addpost(request):
    return render(request, 'pages/addpost.html')

def promoreq(request):
    return render(request, 'pages/promoreq.html')

def update(request):
    return render(request, 'pages/update.html')



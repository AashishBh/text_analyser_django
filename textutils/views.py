from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("hello <h1>World </h1>")

def about(request):
    return HttpResponse("about page")

def analyser(request):

    return render(request,'analyser')

def file(request):
    f = open("textutils/one.txt", "r")
    return HttpResponse(f.read())

def navigator(request):
    return HttpResponse('''
    <h1>My Personal Navigator </h1>
    <p> <a href = "https://www.facebook.com">Facebook </a></p>
    <p> <a href = "https://www.instagram.com">Instagram </p>
    <p> <a href = "https://www.twitter.com">Twitter </p>
    <p> <a href = "https://www.reddit.com">Reddit </p>
    <p> <a href = "https://www.telegram.org">Telegram </p>
    ''')
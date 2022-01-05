from django.http import HttpResponse

def index(request):
    return HttpResponse("hello <h1>World </h1>")

def about(request):
    return HttpResponse("about page")

def one(request):
    f = open("../textutils/one.txt", "r")
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
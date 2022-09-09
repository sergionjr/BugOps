from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>You have arrived on the index for the BugOps proj.<h1>")
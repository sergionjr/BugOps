from django.http import HttpResponse

def index(request):
    return HttpResponse("You have arrived on the index for the BugOps proj.")
from django.shortcuts import HttpResponse,  render

# Create your views here.

def index(request):
    # return HttpResponse(request, 'core/index.html')
    return render(request,'core/index.html')
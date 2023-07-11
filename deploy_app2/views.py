from django.shortcuts import render

def index(request):
    return render(request, 'deploy_app2/index.html')

# Create your views here.

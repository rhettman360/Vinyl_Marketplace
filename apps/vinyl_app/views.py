from django.shortcuts import render
def index(request):
    return render(request, 'vinyl_app/index.html') #end

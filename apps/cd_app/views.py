from django.shortcuts import render
def index(request):
    return render(request, 'cd_app/index.html') #end

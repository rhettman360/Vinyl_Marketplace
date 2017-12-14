from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from forms import VinylForm
from models import Vinyl

def index(request):
    context = {
        'vinyl': Vinyl.objects.all()
    }
    return render(request, 'vinyl_app/index.html', context)

def view(request, vinylid):
    context = {
        'vinyl': Vinyl.objects.get(id=vinylid),
        'vinylurl' : Vinyl.objects.get(id=vinylid).picture.url[14:]
    }
    print Vinyl.objects.get(id=vinylid).picture.url
    print Vinyl.objects.get(id=vinylid).picture.path
    return render(request, 'vinyl_app/view.html', context)

def add(request):
    if request.method == 'POST':
        form = VinylForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/vinyl')
    else:
        form = VinylForm()
        return render(request, 'vinyl_app/add.html', {
        'form': form
    })

def delete(request):
    return render(request, 'vinyl_app/index.html')

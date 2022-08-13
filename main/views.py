from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFile
from .utils import *

def landing(request):
    return render(request, 'main/landing.html')


def file_upload(request):
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            print("sent")
            data = form.cleaned_data
            graph = handleFile(request.FILES['file'], data)
            return render(request, 'main/upload.html', {'form': form, 'graph': graph})
        else:
            print("invalid form")
            
    else:
        form = UploadFile()
    return render(request, 'main/upload.html', {'form': form})

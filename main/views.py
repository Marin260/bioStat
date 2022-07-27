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
            data = form.cleaned_data
            date = data['dateFrom']
            print(type(date))
            handleFile(request.FILES['file'], data['columns'])
            
    else:
        form = UploadFile()
    return render(request, 'main/upload.html', {'form': form})

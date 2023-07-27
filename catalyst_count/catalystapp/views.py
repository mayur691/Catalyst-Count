from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import UploadForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UploadForm()

    return render(request, "upload.html", {"form": form
    })

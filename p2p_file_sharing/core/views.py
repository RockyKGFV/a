from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import File


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('login')  # Redirect to the homepage or another page
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        File.objects.create(user=request.user, file=filename)
        return redirect('file_list')
    return render(request, 'core/upload.html')




@login_required
def file_list(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'core/file_list.html', {'files': files})

@login_required
def download_file(request, file_id):
    file = File.objects.get(id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
    return response
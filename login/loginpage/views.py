from django.shortcuts import render

from .models import lg
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

def lgn(request):
    return render(request, 'lg.html')

def ad(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = lg.objects.filter(username=username, password=password)
        if user:
            messages.success(request, "invalid credentials")
            userdetails = lg.objects.get(username=username, password=password)
            id = userdetails.id
            user_name = userdetails.username
            request.session['id'] = id
            request.session['username'] = user_name
            return render(request, 'ad.html')
        else:
            messages.success(request, "invalid credentials")
            return render(request, 'lg.html')
    else:
        return render(request, 'ad.html')




from django.shortcuts import render,redirect

from django.contrib.auth import login
from .forms import UserCreateForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}')
            return redirect('task_list')
    else:
        form = UserCreateForm()
    return render(request, 'userauth/register.html', {'form': form})


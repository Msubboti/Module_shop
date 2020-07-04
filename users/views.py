
from django.shortcuts import render, redirect


from .forms import RegisterForm
from .models import User
from django.contrib.auth import login
# Create your views here.


def Registration(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('/')
    return render(request, 'costom_registration/register.html', {'form': form})

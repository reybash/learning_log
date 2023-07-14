from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # create the new user account in database and log them in automatically
            # after creation of an account using Django's built-in authentication system (login function).
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = AuthenticationForm(request, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)

                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    if user.role == 'sdm':
                        return redirect('dashboard_sdm')
                    elif user.role == 'officer':
                        return redirect('dashboard_officer')
                    else:
                        return redirect('home')
            else:
                messages.error(request, 'Username atau password salah.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
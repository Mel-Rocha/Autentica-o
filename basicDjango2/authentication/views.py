from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import CustomUser

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            if CustomUser.objects.filter(email=email).exists():
                return render(request, 'registration.html', {'form': form, 'email_exists': True})
            
            form.save()
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form, 'email_exists': False})

def success_view(request):
    return render(request, 'success.html')

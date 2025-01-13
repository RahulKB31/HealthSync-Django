from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_redirect')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def login_redirect(request):
    if request.user.user_type == "PATIENT":
        return redirect('patient_dashboard')
    else:
        return redirect('doctor_dashboard')

@login_required
def patient_dashboard(request):
    return render(request, 'users/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'users/doctor_dashboard.html')












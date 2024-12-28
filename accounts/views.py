from django.shortcuts import render , redirect
from .models import Profile 
from .forms import Signupform
from django.contrib.auth import login , authenticate 
# Create your views here.
def Signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            login(request,user)
            return redirect('/accounts/profile')
            user = authenticate(username=username,password=password)
    else:
        form= Signupform()
    return render(request , 'registration/signup.html' , {'form' : form})

def profile(request):
    pass


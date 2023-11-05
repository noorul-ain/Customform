from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def Sign_up(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        data=User.objects.create_user(first_name=first_name, username=username, last_name=last_name, email=email, password=password1)
        data.save()
        return redirect('login')#this will pass on url name
    return render(request, 'signup.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('next')
    return render(request, 'login.html')
def Next(request):
    return render (request, 'next.html')


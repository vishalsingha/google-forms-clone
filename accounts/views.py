from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.



def register(request):
    if request.method=="POST":
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        if pwd1!=pwd2:
            messages.info(request,'Passwords did not match...', extra_tags='error')
            return render(request , 'index.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already registerd", extra_tags='error')
            return render(request, "index.html")
        else:
            user = User.objects.create_user(username = email.split("@")[0].strip(), email = email, password = pwd1)
            user.save()
        return redirect("login")
    return render(request, "index.html")




def login(request):
    if request.method=="POST":
        email = request.POST['email']
        passward = request.POST['pwd1']
        user = auth.authenticate(username=email.split("@")[0].strip(), password=passward)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials!!!", extra_tags='error')
            return render(request, "login.html")
    return render(request, 'login.html')

def logout_usr(request):
    logout(request)
    return redirect('/')
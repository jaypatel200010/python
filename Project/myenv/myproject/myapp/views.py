from django.shortcuts import render,redirect
from . models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def shop(request):
    return render(request,'shop.html')

def thankyou(request):
    return render(request,'thankyou.html')

def signup(request):
    if request.method== "POST":

        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "Email is already registered!"
            return render(request,'signup.html',{'msg':msg})
        
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password']                  
                )
                return render(request,'login.html')
            else:
                msg = "Password and confirm password does not match!!"
                return render(request,'signup.html',{'msg':msg})

    else:    
        return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])

            if user.password==request.POST['password']:
                request.session['email']=user.email
                return render(request,'index.html')
            else:
                msg = "password does not match!!"
                return render(request,'login.html',{'msg':msg})

        except:
            msg = "Email does not match!"
            return render(request,'login.html',{'msg':msg})

    else:
        return render(request,'login.html')
    
def logout(request):
    del request.session['email']
    return redirect('login')

def cpass(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.session['email'])

            if user.password==request.POST['password']:
                if request.POST['npassword']==request.POST['cnpassword']:
                    user.password=request.POST['npassword']
                    user.save()
                    return redirect('logout')
                else:
                    msg = "Pass and confirm pass does not match!!"
                    return render(request,'cpass.html',{'msg':msg})
            else:
                msg = "old pass does not match!!"
                return render(request,'cpass.html',{'msg':msg})
            
        except:
            return render(request,'cpass.html')

    else:
        return render(request,'cpass.html')
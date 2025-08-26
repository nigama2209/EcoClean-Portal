import uuid
from django.shortcuts import render,redirect # type: ignore
from django.http import HttpResponse # type: ignore
from common.models import ContactForm
from common.models import userregistration
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash # type: ignore
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def main(request):
    return render(request, 'HomePage/main.html')
def services(request):
    return render(request, 'HomePage/services.html')
def portfolio(request):
    return render(request, 'HomePage/portfolio.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['en']
        email= request.POST['ee']
        phone = request.POST['pn']
        msg=request.POST['sendmessage']
        details=ContactForm(Name=name,EmailId=email,PhoneNumber=phone,Message=msg)
        details.save()
        return render(request, 'HomePage/contact.html',{'message':'Sent'})
    else:
        return render(request, 'HomePage/contact.html',{'message':''})
def customlogin(request):
    if request.method == 'POST':
        emorph = request.POST['ep']
        password = request.POST['pass']
        if not User.objects.filter(username=emorph).exists():
            messages.error(request,'Invalid Username')
            return redirect('/')
        user = authenticate(username=emorph, password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/')
        else:
            ur=userregistration.objects.filter(username=emorph)
            if ur.exists():
                login(request,user)
                return redirect('/customer')
    return render(request, 'Login/login.html')
def signup(request):
    if request.method == 'POST':
        uname = request.POST['names']
        usernames=request.POST['username']
        uemail= request.POST['emails']
        phones = request.POST['phn']
        upassword=request.POST['passw']
        conpassword=request.POST['cpassw']
        address=request.POST['add']
        if upassword == conpassword:
            user = User.objects.filter(username=usernames) 
            if user.none:
                useradd=User.objects.create_user(first_name=uname,username=usernames)
                useradd.set_password(upassword)
                useradd.save()
                userid = uuid.uuid4().hex[:8]
                storedata=userregistration(Name=uname,username=usernames,EmailId=uemail,PhoneNumber=phones,address=address,userid=userid)
                storedata.save()
                return render(request,'Login/login.html')
            else:
                return render(request,"Login/signup.html",{'message':'user exists'})
        else:
            return render(request,"Login/signup.html",{'message':'password did not match'})
    else:
        return render(request,'Login/signup.html',{'message':''})
def reset(request):
    if request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['npassword']
        confirm_password = request.POST['cpassword']   # confirm password

        if new_password != confirm_password:
            return render(request, 'Login/reset.html', {'message': 'Passwords do not match!'})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'Login/reset.html', {'message': ' User not found!'})

        # set new password
        user.set_password(new_password)
        user.save()

        return render(request, 'Login/reset.html', {'message': 'Password reset successful! Please login again.'})

    return render(request, 'Login/reset.html', {'message': ''})

def abtad(request):
    return render(request, 'HomePage/abtad.html')
def abtman(request):
    return render(request, 'HomePage/abtman.html')
def abtcust(request):
    return render(request, 'HomePage/abtcust.html')
def subscribe(request):
    subject=request.POST['sub']
    return render(request, 'HomePage/main.html')



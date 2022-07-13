
# import pdb;
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import empleave_model
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import empleave_form
from django.core.mail import send_mail  
from django.conf import settings
from django.contrib.auth import login,authenticate
from django.http import JsonResponse

# Create your views here.
def empregister_view(request):
    # print(request.user)

    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['em']
        username=request.POST['unm']
        password=request.POST['pswd']
        confirm_password=request.POST['pswd2']

        #validation..

        if name and email and username and password and confirm_password == ' ':
            return HttpResponse ('all fields required..')
            # return redirect('empregister')

        if len(name)>10:
            messages.error(request,'username must be under 10 character')
            return redirect('empregister')

        if not name.isalpha():
            messages.error(request,'username should only contain 10 characters')
            return redirect('empregister')


        if password!=confirm_password:
            messages.error(request,'Confirm Password do not match with Password')
            return redirect('empregister')

        

        create_user=User.objects.create_user(username,email,password)
        create_user.first_name=name
        create_user.save()
        messages.success(request,'user registered successfully..')
        return redirect('emplogin')

    else:
        return render(request,'emp_register.html')


def emplogin_view(request):
    if request.method=='POST':
        username=request.POST['unm']
        password=request.POST['pswd']
        user=authenticate(username=username,password=password)
        
        if user is not None:
        
            login(request,user)
            if user.is_superuser :    
                 
                 return redirect('displayadmin')
            else:
                messages.success(request,'you have successfully logged in...')
                return redirect('displayuser')     
    else:
        return render(request,'emp_login.html')


def displayuser_view(request):
    getdata=User.objects.get(pk=request.user.pk) 
    context={'getdata':getdata}
    return render(request,'display_user.html',context)



def displayadmin_view(request):
    getuserdata =User.objects.all()
    getleavedata=empleave_model.objects.all()
    user_count = User.objects.count()
    return render(request,'display_admin.html',{'getuserdata':getuserdata,'user_count':user_count,'getleavedata':getleavedata})


def approve_view(request,id):
    if request.method == 'POST':
        if request.POST.get('approve_btn') == "Approve":
            var=list(empleave_model.objects.filter(id=id).values('email'))
            subject='LEAVE'
            msg="approved"
            to=var[0]['email']
            res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
            if (res==1):
                msg='sent mail successfully'
            else:
                msg='mail could not sent'
            # return render(request,'displayuser.html',{'var':var})
            return HttpResponse(msg)
            # return JsonResponse(var,safe=False)
    
        else:
            return HttpResponse('error')    
            
            
def home_view(request):
    return render(request,'home.html') 


def reject_view(request,id):
    if request.method == 'POST':
        if request.POST['reject_btn'] == "Reject":
            var=list(empleave_model.objects.filter(id=id).values('email'))
            subject='LEAVE'
            msg="rejected"
            to=var[0]['email']
            res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
            if (res==1):
                msg='sent mail successfully'
            else:
                msg='mail could not sent'
            return HttpResponse(msg)
            # return JsonResponse(var,safe=False)
        else:
            return HttpResponse('error')   

     

def empleave_view(request):
    form=empleave_form
    if request.method=='POST':
        form=empleave_form(request.POST)
        if form.is_valid():
            name=request.POST['name']   
            form.save()
            subject='Applied For Leave'
            msg=f"I'm {name}, applied for leave. can i take leave?"
            to='mehtariti82@gmail.com'
            res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
            if (res==1):
                msg='sent mail successfully'
            else:
                msg='mail could not sent'
            return redirect('home')
        else:
            print('error')     
    return render(request,'apply_empleave.html',{'f':form})
    
    


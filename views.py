from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import images

# Create your views here.

def firstpage(request):
    return render(request,'firstpage.html')

#def Marklabel(request):
#    data=User.objects.all()
#    return render(request,'Marklabel.html',{'users':data,})

def Marklabel(request):
    data=User.objects.all()
    return render(request,'Marklabel.html',{'users':data,})

def MarklabelForm(request,id):
    if request.method =='GET':
        Imagesupload = images.objects.all()
    return render(request, 'pictures.html',{'images_upload' : Imagesupload })

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/upload')
    else:
        form = ImageForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def manageForm(request):
    data=User.objects.all()
    return render(request,'manageForm.html',{'users':data,})

def createForm(request):
    data=Post.objects.all()
    return render(request,'index.html',{'posts':data})

def Register(request):
      return render(request,'Register.html')

def addUser (request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password==repassword:
        if User.objects.filter(username = username).exists():
            messages.info(request,'Username มีคนใช้แล้ว')
            return redirect ('/page2')
        elif User.objects.filter(email = email).exists():
            messages.info(request,'Email มีคนใช้แล้ว')
            return redirect('/page2')
        else:
            user = User.objects.create_user(
                 username=username,
                 password=password,
                 email=email,
                 first_name=firstname,
                 last_name=lastname
             )
            user.save()
            return redirect('/')
    else:
        messages.info(request, 'Password ไม่ตรงกัน')
        return redirect('/page2')


def loginForm (request):
     return render(request,'login.html')

def login(request):
    username = request.POST["username"]
    password = request.POST['password']

    #Check username password
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profileUser(request):
    data = User.objects.all()
    return render(request,'Userprofile.html')

def deleteAccount(request,id):
    data = User.objects.get(id=id) # user =Test001
    data.delete()
    return redirect ("/manageForm")

def deleteConfirm(request):
    user=auth.authenticate()
    if user is not None:      
        return render(request,'manageForm.html')
    else:
        return render(request,'manageForm.html')

def deleteCancle(request):
    user=auth.authenticate()
    if user is not None:    
        return render(request,'manageForm.html')
    else:
        return render(request,'manageForm.html')

def upload(request): 
  
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save()
            img_obj =form.instance
            return render(request, 'pictures.html',{'form' : form, 'img_obj' : img_obj }) 
    else: 
        form = ImageForm() 
    return render(request, 'upload.html', {'form' : form}) 

def pictures(request):
    return render(request,'pictures.html')








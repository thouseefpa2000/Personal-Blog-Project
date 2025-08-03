from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from.forms import RegisterForm,blogForm,praticeForm
from .models import blogModel,praticeModel
# Create your views here.
def base(request):
    return render(request,'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Ensure 'index' is defined in your `urls.py` via `name='index'`
        else:
            # Optional: Add error handling here
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
from django.shortcuts import render, redirect
from .forms import RegisterForm  # Make sure this import is correct

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Use the name of your login URL here
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def myblog(request):
    blog=blogModel.objects.all()
    return render(request,'myblog.html',{'blog':blog})




def pratice(request):
    ps = praticeModel.objects.all()  
    return render(request, 'pratice.html', {'ps': ps})  

def answer(request):
    ps = praticeModel.objects.all()  
    return render(request, 'answer.html', {'ps': ps})  

def dashboard(request):
    return render(request, 'dashboard.html') 
    
    
# crud here
def blogCreate(request):
    form=blogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myblog')
    return render(request,'createblog.html',{'form':form})


def deleteblog(request,pk):
    dl=blogModel.objects.get(pk=pk)
    dl.delete()
    return redirect('myblog')


def readblog(request,pk):
    blog=blogModel.objects.get(pk=pk)
    return render(request,'readmore.html',{'blog':blog})

def updateblog(request,pk):
    blog=blogModel.objects.get(pk=pk)
    form=blogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('myblog')
    return render(request,'updateblog.html',{'form':form})



from django.db.models import Q

def myblog(request):
    query = request.GET.get('q')
    if query:
        blog = blogModel.objects.filter(
            Q(title__icontains=query) | Q(decription__icontains=query)
        )
    else:
        blog = blogModel.objects.all()
    return render(request, 'myblog.html', {'blog': blog})

# views.py
def createpratice(request):  # ← remove `pk`
    form = praticeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pratice')
    return render(request, 'createpratice.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect


def deletepratice(request, pk):
    dl = get_object_or_404(praticeModel, pk=pk)
    dl.delete()
    return redirect('pratice')  # This assumes you have a 'pratice' view

def deletepratice(request,pk):
    pass

def pratice(request):
    ps = praticeModel.objects.all()
    return render(request, 'pratice.html', {'ps': ps})

def answer(request, pk):
    ps = praticeModel.objects.get(pk=pk)
    return render(request, 'answer.html', {'ps': ps})

def updatepratice(request,pk):
    pratice=praticeModel.objects.get(pk=pk)
    form=praticeForm(request.POST or None, instance=pratice)
    if form.is_valid():
        form.save()
        return redirect('pratice')
    return render(request,'updatepratice.html',{'form':form})
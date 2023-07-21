from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import Blogform


# Create your views here.
def index(request):
    return render(request,'index.html')


def home(request):
    if request.method=='GET':
        data = Branch.objects.all()
        return render(request,'home.html',{"data":data})
    else:
        name=request.POST['name']
        age=request.POST['age']
        branch= Branch.objects.get(branch= request.POST['branch'])
        ab=Student(name=name,age=age,branch=branch)
        ab.save()
        return render(request,'home.html')      

        
def show(request): 
    dat=Branch.objects.all()
    data = Student.objects.all()
    return render (request,'show.html',{'dat':dat,"data":data})
    
def filterbranch(request,branch):
    b = Branch.objects.get(branch=branch)
    data = Student.objects.filter(branch=b)
    dat=Branch.objects.all()
    return render(request,'show.html',{'data':data,'dat':dat})

def fit(request):
    if request.method=='GET':
        form=Blogform()
        
        
        return render(request,'addblog.html',{'form':form})
    else:
        form=Blogform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('fit')
def seen(request):
    see=Blog.objects.all()
    return render(request,'seen.html',{'see':see})



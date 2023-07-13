from django.shortcuts import render,HttpResponse
from .models import student

# Create your views here.
def home(request):
    return HttpResponse('My NAme is Aman')

def ind(request):
    if request.method=='GET':
              name='aman'

              return render(request,'index.html',{'base':name})
    else:
        pro=request.POST['pr']
        midd=request.POST['mid']
        senn=request.POST['sen']
        colll=request.POST['coll']

        return render(request,'index.html',{'pro':pro,'midd':midd,'senn':senn,'colll':colll})
    
def abc(request):
      if request.method=='GET':
        return render(request,'home.html')
      else:
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        school=request.POST['school']
        std=request.POST['std']
        data=student(name=name,age=age,email=email,school=school,std=std)
        data.save()
        return render(request,'home.html')


    
def show(request):
     data=student.objects.all
     return render(request,'show.html',{'data':data})


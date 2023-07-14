from django.shortcuts import render,HttpResponse,redirect
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

def delete(request,id):
    student.objects.get(id=id).delete()
    return redirect('show')



def update(request,id):
    if request.method=='GET':
      data = student.objects.get(id=id)  
      return render(request,'home.html',{'data':data})
    
    else:
      name=request.POST['name']
      age=request.POST['age']
      email=request.POST['email']
      school=request.POST['school']
      std=request.POST['std']
      data=student(id=id,name=name,age=age,email=email,school=school,std=std)
      data.save()
      return redirect('show')

    



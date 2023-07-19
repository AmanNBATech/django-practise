from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *

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
     data=student.objects.get(id=id)
     data.delete()
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

def veh(request):
    if request.method=='GET':
        inform = vehcile.objects.all()
        return render(request, 'veh.html', {'info': inform})
        
    
    
    else:
      mode=request.POST['mode']
      year=request.POST['year']
      reg=request.POST['reg']
      color=request.POST['color']
      cost=request.POST['cost']
      fuel=request.POST['fuel']

      info=vehcile(mode=mode,myear=year,reg_no=reg,color=color,cost=cost,fuel=fuel)
      info.save()
      inform=vehcile.objects.all()
      return render(request,'veh.html',{'info':inform})


def dele(request,id):
   
     vehcile.objects.get(id=id).delete()
     return redirect('veh')

def edit(request,id):
    if request.method == 'GET':
  
        info=vehcile.objects.get(id=id)
        inform=vehcile.objects.all()
        return render(request, 'veh.html', {'info':inform,'main':info})
    else:
        mode = request.POST['mode']
        year = request.POST['year']
        reg = request.POST['reg']
        color = request.POST['color']
        cost = request.POST['cost']
        fuel = request.POST['fuel']

        info = vehcile(id = id,mode=mode, myear=year, reg_no=reg, color=color, cost=cost, fuel=fuel)
        info.save()
        
        inform=vehcile.objects.all()
        return redirect('veh')
        
        # return render(request,'veh.html',{'info':inform})

    


def djangoform(request):
    if request.method=='GET':
        form=vehcileform()
        
        return render(request,'djangoform.html',{'form':form})
    else:
        form=vehcileform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('djangoform')
    
def sport(request):
    if request.method=='GET':
        form=sportsform()
        ib=sports.objects.all()
        return render(request,'sports.html',{'form':form,'ib':ib})
    else:
        form=sportsform(request.POST)
        if form.is_valid():
            form.save()
            ib=sports.objects.all()
            
            return redirect('sport')

def move(request,id):
    sports.objects.get(id=id).delete()
    return redirect('sport')

    
def change(request,id): 
    emp = sports.objects.get(id=id)  
    if request.method=='GET':
        form=sportsform(instance=emp)
        ibc=sports.objects.all()
        return render(request,'sports.html',{'form':form,'ib':ibc})
    else:
        form=sportsform(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('sport')
        

    # if request.method=='POST':
    #   form = sportsform(request.POST, instance = emp)  
    # return render(request, 'sports.html', {'form':form})  

    # if form.is_valid():  
    #     form.save()  
        
    #     return redirect("/sport") 
     
    # return render(request, 'sports.html', {'emp': emp,'form':form})  
        


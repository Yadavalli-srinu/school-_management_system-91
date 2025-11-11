from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import staff_model,student_model,fee_model
from app1.forms import staff_form, student_form, fee_form
from app1.forms1 import staff_update_form, student_update_form, fee_update_form


def opening_table(request):
   return render(request,"frontend_app1/main_page.html")



def staff_table(request):
    data = staff_model.objects.all()
    content={
       "data":data
    }
    return render(request, 'frontend_app1/staff_table.html',content)


 


 

def add_staff(request):
    if request.method=="POST":
        form = staff_form(request.POST)
        if form.is_valid():
           form.save()
           return redirect('stafftable')
        else:
          return HttpResponse("Invalid Email")
    else:
        form = staff_form()
        content={
        "form":form,
         }
        return render(request,'frontend_app1/add_staff1.html',content)

def update_staff(request,id):
    data = staff_model.objects.get(id=id)
    if request.method=="POST":
       form=staff_update_form(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect('stafftable')
    else:
       form = staff_update_form(instance=data)
       content={
        "form":form,
         }
       return render(request,'frontend_app1/update_staff.html',content)
    
def delete_staff(request,id):
   data=staff_model.objects.get(id=id)
   data.delete()
   return redirect('stafftable')
       


def student_table(request):
    data = student_model.objects.all()
    content={
       "data":data
    }
    return render(request, 'frontend_app1/student_table.html',content)

def add_student(request):
    if request.method=="POST":
        form = student_form(request.POST)
        if form.is_valid():
           form.save()
           return redirect('studenttable')
        else:
          return HttpResponse("Invalid Email")
    else:
        form= student_form()
        content={
        "form":form,
         }
        return render(request,'frontend_app1/add_student1.html',content)

def update_student(request,id):
    data = student_model.objects.get(id=id)
    if request.method=="POST":
       form=student_update_form(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect('studenttable')
    else:
       form = student_update_form(instance=data)
       content={
        "form":form,
         }
       return render(request, 'frontend_app1/update_student.html',content)
    
def delete_student(request,id):
   data=student_model.objects.get(id=id)
   data.delete()
   return redirect('studenttable')
       




def fee_table(request):
    data = fee_model.objects.all()
    content={
       "data":data
    }
    return render(request, 'frontend_app1/fee_table.html',content)


def add_fee(request):
    if request.method=="POST":
        form = fee_form(request.POST)
        if form.is_valid():
           form.save()
           return redirect('feetable')
        else:
          return HttpResponse("Invalid Email")
    else:
        form = fee_form()
        content={
        "form":form,
         }
        return render(request,'frontend_app1/add_fee1.html',content)

def update_fee(request,id):
    data = fee_model.objects.get(id=id)
    if request.method=="POST":
       form=fee_update_form(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect('feetable')
    else:
       form = fee_update_form(instance=data)
       content={
        "form":form,
         }
       return render(request, 'frontend_app1/update_fee.html',content)
def delete_fee(request,id):
   data=fee_model.objects.get(id=id)
   data.delete()
   return redirect('feetable') 
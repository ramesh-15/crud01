from django.shortcuts import render,HttpResponse,redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def emp(request):
    try:
        if request.method=="POST":
            id=request.POST.get('id')
            name=request.POST.get('name')
            email=request.POST.get('email')
            contact=request.POST.get('contact')
            data = Employee(eid=id,ename=name,eemail=email,econtact=contact)
            data.save()
            return render(request, 'index.html', {'info': 'Inserted successfull...'})
        else:
            return render(request,'index.html')
    except:
        return render(request,'index.html',{'info':'Fill all required fields...'})

def show(request):
    employee = Employee.objects.all()
    return render(request,'show.html',{'employees':employee})


def edit(request,id):
    employee = Employee.objects.get(eid=id)
    return render(request,'edit.html')

def update(request,id):
    employee = Employee.objects.get(eid=id)
    form = EmployeeForm(request.POST,instance = employee)
    if request.method=="POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        data = Employee(eid=id, ename=name, eemail=email, econtact=contact)
        data.save()

        return render(request,'show.html')
    else:
        return render(request,'edit.html',{'employee':employee})

def destroy(request):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return render(request,'show.html')




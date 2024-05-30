from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
# Home View
def home(request):
    return render(request,"home.html")
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
    # #return HttpResponse("Hello World")


# Players View
def players(request):
    template = loader.get_template('players.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello World")



def contactus(request):
     return render(request,"contact.html")



def emp(request):
	if request.method == "POST":
		form = EmployeeForm (request.POST) # here "form" is one varible
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:
		form = EmployeeForm()
	return render(request,"index.html",{'form':form})


def show(request):
	employees = Employee.objects.all() # it's select query,select all data store in employees varible
	return render(request,"show.html",{'employees': employees})

def edit(request,id):
	employee = Employee.objects.get(id=id)
	return render(request,"edit.html",{'employee':employee})

def update(request,id):
	employee = Employee.objects.get(id=id)
	form = EmployeeForm(request.POST, instance=employee)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request,"edit.html",{'employee':employee})

def delete(request,id):
	employee = Employee.objects.get(id=id)
	employee.delete()
	return redirect("/show")

def home(request):
	return render(request,"home.html")




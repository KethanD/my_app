from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Customer, CustomerComms
from . forms import NewCustomerForm, AddCustomerCommsForm

def add_customer_comms(request):

	form = AddCustomerCommsForm()

	if request.method == 'POST':

		form = AddCustomerCommsForm(request.POST)
		
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('add_customer_comms', )

	else:
		form =  AddCustomerCommsForm()

		return render(request, 'customer_create.html', {"form": form})



def customer_create(request):
		
	if request.method == 'POST':

		form = NewCustomerForm(request.POST)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('add_customer_comms', )

	else:
		form =  NewCustomerForm()
	return render(request, 'customer_create.html', {"form": form})

def index(request):
	return render(request, 'index.html', {})


def show_customer_details(request, customer_id):
	customer = Customer.objects.get(pk=customer_id)
	return render(request, 'show_customer_details.html', {'customer': customer})

def list_customers(request):
	customer_list = Customer.objects.all()
	return render(request, 'customer_list.html', {'customer_list': customer_list})
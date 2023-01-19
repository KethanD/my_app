from django import forms
from django.forms import ModelForm
from .models import Customer, CustomerComms

class NewCustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('customer_project_name', 'onboarded_on', 'authorisation_preference',
					'customer_id', 'h2h_user_id', 'countries_involved', 'capability_required' )

		widgets = {
		'customer_project_name':forms.TextInput(attrs={'class': 'form-control'}),
		'onboarded_on':forms.Select(attrs={'class': 'form-control'}),
		'authorisation_preference':forms.TextInput(attrs={'class': 'form-control'}),
		'customer_id':forms.TextInput(attrs={'class': 'form-control'}),
		'h2h_user_id':forms.TextInput(attrs={'class': 'form-control'}),
		
		'countries_involved':forms.CheckboxSelectMultiple(attrs=
			{'class': 'form-control', 
			 'class': 'form-check-inline',
			 'class': 'display-6'}
			 ),
		
		'capability_required':forms.CheckboxSelectMultiple(attrs=
			{'class': 'form-control',
			'class': 'form-check-inline',
			'class': 'display-6'}
			),
		}


class AddCustomerCommsForm(ModelForm):
	class Meta:
		model = CustomerComms
		fields = ('customer_name', 'sending_channel', 'recieving_channel', 'transport_protocol', 'production_ip', 
			'test_env_ip', 'dr_env_ip', 'production_port', 'test_env_port', 'dr_env_port')

		widgets = {
				'customer_name': forms.Select(attrs={'class': 'form-control'}), 
				'sending_channel': forms.Select(attrs={
					'class': 'form-control',
					'class': 'form-check-inline',
					
					}) , 
				'recieving_channel':forms.Select(attrs={
					'class': 'form-control',
					'class': 'form-check-inline',
					}), 
				'transport_protocol':forms.Select(attrs={
					'class': 'form-control',
					'class': 'form-check-inline',
					}),
				'production_ip': forms.TextInput(attrs={
					'class': 'form-control',
					'class': 'row g-1',
					'class': 'col-sm-7',
					'class': 'bg-primary-subtle',
					}) , 
				'test_env_ip':forms.TextInput(attrs={
					'class': 'form-control',
					'class': 'row g-3',
					'class': 'col-sm-7',
					}) , 
				'dr_env_ip': forms.TextInput(attrs={
					'class': 'form-control',
					'class': 'row g-3',
					'class': 'col-sm-7',
					}), 
				'production_port':forms.NumberInput(attrs={
					'class': 'form-control',
					'class': 'row g-3',
					'class': 'col-sm-2',
					}), 
				'test_env_port':forms.NumberInput(attrs={
					'class': 'form-control',
					'class': 'row g-3',
					'class': 'col-sm-2',					
					}), 
				'dr_env_port':forms.NumberInput(attrs={
					'class': 'form-control',
					'class': 'row g-3',
					'class': 'col-sm-2',
					})
		}
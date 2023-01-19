import datetime
from django.db import models
from multiselectfield import MultiSelectField



class Customer(models.Model):
	onboarded_choices = {
		('BOL', 'BOL'),
		('nBOL', 'nBOL')
		}

	countries_involved = (
		('AO','Angola'),
		('KE', 'Kenya'),
		('MZN', 'Mozambique'),

		)

	capability_required = {
		('Account Management', 'Account Management'),
		('Payments', 'Payments'),
		('Collections', 'Collections')
		}

	customer_project_name = models.CharField(max_length=100)
	date_added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	onboarded_on = models.CharField(max_length=5, choices=onboarded_choices)

	authorisation_preference = models.CharField(max_length=20)
	customer_id = models.CharField(max_length=30)
	h2h_user_id = models.CharField(max_length=20)

	countries_involved =  MultiSelectField(choices=countries_involved, max_length=20)

	capability_required = MultiSelectField(max_length=40, choices=capability_required)


	def __str__(self):
		return self.customer_project_name 


class CustomerComms(models.Model):
	sending_channel = [
			('Public', 'Public'),
			('VPN', 'VPN'),

	]
	
	recieving_channel = [
			('Public', 'Public'),
			('VPN', 'VPN'),
	]

	transport_protocol_choices = [
			('SFTP-Push/Pull', 'SFTP-Push/Pull'),
			('SFTP-Push/Push', 'SFTP-Push/Push'),
			('Connect Direct', 'Connect Direct'),
			('SWIFT-File-Act', 'SWIFT-File-Act'),

	]

	customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	sending_channel = models.CharField(max_length=10, choices=sending_channel)
	recieving_channel = models.CharField(max_length=10, choices=recieving_channel)

	transport_protocol = models.CharField(max_length=20, choices=transport_protocol_choices)

	production_ip = models.GenericIPAddressField()
	test_env_ip = models.GenericIPAddressField()
	dr_env_ip = models.GenericIPAddressField()
	production_port = models.IntegerField()
	test_env_port = models.IntegerField()
	dr_env_port = models.IntegerField()

	def __str__(self):
		return str(self.customer_name) 
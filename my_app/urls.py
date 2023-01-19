from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('customer_create', views.customer_create, name='customer_create'),
    path('add_customer_comms', views.add_customer_comms, name='add_customer_comms'),
    path('list_customers', views.list_customers, name='list_customers'),
    path('show_customer_details/<customer_id>', views.show_customer_details, name='show_customer_details'),
]
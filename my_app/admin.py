from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from .models import Customer, CustomerComms


#admin.site.register(Customer)
#admin.site.register(CustomerComms)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_project_name', 'date_added', 'customer_id', 'h2h_user_id', 'countries_involved', 'capability_required', 'link_cust_comms')
    ordering = ('customer_project_name',)
    search_fields = ('customer_project_name',)

    def link_cust_comms(self, Customer):
    #  https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html
    # https://github.com/gitaarik/django-admin-relation-links
    #    customer = Customercomms.get(pk.customer_name)
    #   url = reverse('admin:my_app_link_cust_comms',
    #        args= [customer.customercomms.id])
    #    return format_html('<a href="{}">{}</a>', url, customer.customercomms.name)
    #link_cust_comms.short_description = 'Customer Comms'   
     pass        


@admin.register(CustomerComms)
class CustomerCommsAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'sending_channel', 'recieving_channel', 
                    'production_ip', 'production_port',
                    'test_env_ip', 'test_env_port', 
                    'dr_env_ip', 'dr_env_port',
                    'updated', 'date_added'
                     )
    search_fields = ['customer_name__customer_project_name',]



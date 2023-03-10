# Generated by Django 4.1.4 on 2022-12-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_rename_customer_name_customercomms_customer_project_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customercomms',
            old_name='customer_project_name',
            new_name='customer_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='capability_required',
            field=models.CharField(choices=[('Account Management', 'Account Management'), ('Collections', 'Collections'), ('Payments', 'Payments')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='countries_involed',
            field=models.CharField(choices=[('MZN', 'Mozambique'), ('AO', 'Angola'), ('KE', 'Kenya')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='onboarded_on',
            field=models.CharField(choices=[('BOL', 'BOL'), ('nBOL', 'nBOL')], max_length=5),
        ),
    ]

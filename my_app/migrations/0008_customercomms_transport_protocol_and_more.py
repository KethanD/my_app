# Generated by Django 4.1.4 on 2022-12-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_alter_customer_capability_required_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercomms',
            name='transport_protocol',
            field=models.CharField(choices=[('SFTP-Push/Pull', 'SFTP-Push/Pull'), ('SFTP-Push/Push', 'SFTP-Push/Push'), ('Connect Direct', 'Connect Direct'), ('SWIFT-File-Act', 'SWIFT-File-Act')], default='SFTP-Push/Pull', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='capability_required',
            field=models.CharField(choices=[('Collections', 'Collections'), ('Account Management', 'Account Management'), ('Payments', 'Payments')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='countries_involed',
            field=models.CharField(choices=[('KE', 'Kenya'), ('AO', 'Angola'), ('MZN', 'Mozambique')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='onboarded_on',
            field=models.CharField(choices=[('nBOL', 'nBOL'), ('BOL', 'BOL')], max_length=5),
        ),
    ]

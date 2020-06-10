# Generated by Django 3.0.4 on 2020-04-14 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0004_auto_20200414_2242'),
        ('accounts', '0003_remove_accountuser_org_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='org_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='org.OrgOwner'),
        ),
    ]
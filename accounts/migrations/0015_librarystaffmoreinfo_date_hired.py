# Generated by Django 3.2 on 2023-07-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_remove_librarystaffmoreinfo_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarystaffmoreinfo',
            name='date_hired',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date Hired'),
        ),
    ]

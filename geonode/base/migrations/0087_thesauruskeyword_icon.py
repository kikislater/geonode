# Generated by Django 3.2.22 on 2023-10-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0086_linkedresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesauruskeyword',
            name='icon',
            field=models.CharField(blank=True, max_length=512, null=True, help_text='It can be a fa-class name or a URL to an image'),
        ),
    ]
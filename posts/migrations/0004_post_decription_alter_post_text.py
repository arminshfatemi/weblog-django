# Generated by Django 4.2.1 on 2023-05-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='decription',
            field=models.CharField(blank=True, max_length=95, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='no text :(', max_length=400),
        ),
    ]

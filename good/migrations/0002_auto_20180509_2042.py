# Generated by Django 2.0.5 on 2018-05-09 12:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goodBorrowerId', to='user.User'),
        ),
        migrations.AlterField(
            model_name='good',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='good',
            name='release_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sharerequest',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sharerequest',
            name='request_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='sharerequest',
            name='state',
            field=models.CharField(default='未处理', max_length=10, null=True),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-14 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=120, unique=True)),
                ('description', django_quill.fields.QuillField()),
                ('logo', models.CharField(blank=True, max_length=400, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-14 12:55

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_course_date_modified_course_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=120)),
                ('description', django_quill.fields.QuillField()),
                ('video', models.CharField(blank=True, max_length=400, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.course')),
            ],
        ),
    ]
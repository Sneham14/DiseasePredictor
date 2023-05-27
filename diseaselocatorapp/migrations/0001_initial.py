# Generated by Django 3.2.11 on 2023-04-24 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctorprofile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('registration_no', models.CharField(max_length=20)),
                ('year_of_registration', models.DateField()),
                ('qualification', models.CharField(max_length=20)),
                ('State_Medical_Council', models.CharField(max_length=30)),
                ('specialization', models.CharField(max_length=30)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patientprofile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('is_patient', models.BooleanField(default=True)),
                ('is_doctor', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='rating_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('review', models.TextField(blank=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diseaselocatorapp.doctorprofile')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diseaselocatorapp.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Diseaseinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseasename', models.CharField(max_length=200)),
                ('no_of_symp', models.IntegerField()),
                ('symptomsname', models.TextField(verbose_name=models.CharField(max_length=200))),
                ('confidence', models.DecimalField(decimal_places=2, max_digits=5)),
                ('consultdoctor', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diseaselocatorapp.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('diseaseinfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diseaselocatorapp.diseaseinfo')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diseaselocatorapp.doctorprofile')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diseaselocatorapp.patientprofile')),
            ],
        ),
    ]

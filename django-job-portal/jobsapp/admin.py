from django.contrib import admin

# Register your models here.
from jobsapp.models import Applicant, Job

admin.site.register(Job)
admin.site.register(Applicant)
from django.contrib import admin

# Register your models here.
from accounts.models import User,Message

admin.site.register(User)
admin.site.register(Message)
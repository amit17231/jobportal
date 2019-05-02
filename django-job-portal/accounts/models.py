from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)



class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    contact_no = models.IntegerField(blank=True)
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()

class Message(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Subject= models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
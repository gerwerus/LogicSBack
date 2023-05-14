from django.conf import settings
from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=255)
    table = JSONField()
    simElements = JSONField()
    def __str__(self):
        return self.title

class StudentUser(AbstractUser):
    first_name = models.CharField(
        ("first_name"),
        max_length=30,
    )
    last_name = models.CharField(
        ("last_name"),
        max_length=30,
    )
    group = models.ForeignKey('Group', on_delete=models.PROTECT)
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'group']
    
    def __str__(self):
        return self.username

class StudentTest(models.Model):
    passTime = models.DateTimeField(auto_now_add=True)
    passTest = models.ForeignKey('Test', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey('StudentUser', on_delete=models.CASCADE)
    attempts = models.IntegerField(default=0)
    succses = models.BooleanField(default=False)
    def __str__(self):
        return self.user

class Group(models.Model):
    name = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.name


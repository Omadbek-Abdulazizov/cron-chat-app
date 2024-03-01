from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Lavozimlar(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.title

class Hodimlar(models.Model):
    lavozimi = models.ForeignKey(Lavozimlar, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    telegram_id = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Shablonlar(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    
class Habarlar(models.Model):
    hodim = models.ManyToManyField(Hodimlar, blank=True)
    text = models.TextField()
    vaqt = models.DateTimeField(blank=True, null=True)
    
    




class User(AbstractUser):
    # ...
    groups = models.ManyToManyField(Group, verbose_name='groups', related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', related_name='custom_user_set')

class Admin(models.Model):
    # ...
    groups = models.ManyToManyField(Group, related_name='custom_admin_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_admin_set')
    
    def __str__(self) -> str:
        return self.username
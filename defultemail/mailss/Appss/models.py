from django.db import models

# Create your models here.


class UserOTP(models.Model):
    otp = models.IntegerField()
    is_verified = models.IntegerField(default=False)

    # def __str__(self):
    #   return self.otp
class UserDetail(models.Model):
    name = models.CharField(max_length=100,default=None)
    email =models.EmailField(max_length=100, default=None) 
    message =models.TextField(max_length=1000) 
    subject =models.TextField(max_length=1000, default=None) 
    from_email = models.EmailField(max_length=100,default=None)  
    file = models.FileField(default=None) 
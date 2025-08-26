from django.db import models
# Create your models here.
class ContactForm(models.Model):
    Name = models.CharField(max_length=25)
    EmailId = models.EmailField()
    PhoneNumber = models.IntegerField()
    Message = models.TextField(max_length=225)
class adminprofile(models.Model):
    Name = models.CharField(max_length=25)
    EmailId = models.EmailField()
    PhoneNumber = models.IntegerField()
class addbranch(models.Model):
    branchname = models.CharField(max_length=25)
    branchId = models.IntegerField()
    Branchadd = models.CharField(max_length=50)
class clothtype(models.Model):
    typeofcloth=models.CharField(max_length=40)
    def __str__(self):
        return self.typeofcloth
class servicename(models.Model):
    servicename=models.CharField(max_length=40)
    def __str__(self):
        return self.servicename
class addservice(models.Model):
    servicename=models.ForeignKey(servicename,on_delete=models.PROTECT,default=1)
    typeofcloth=models.ForeignKey(clothtype,on_delete=models.PROTECT,default=1)
    price=models.IntegerField()
class userregistration(models.Model):
    Name = models.CharField(max_length=25)
    username = models.CharField(max_length=40)
    EmailId = models.EmailField()
    PhoneNumber = models.IntegerField()
    address = models.CharField(max_length=100)
    userid=models.CharField(max_length=10)






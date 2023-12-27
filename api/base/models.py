from django.db import models

# Create your models here.

class Company(models.Model): #we are going to create relationship bw advocates and companies
    name = models.CharField(max_length=250)  # The company's official name.
    bio=models.TextField(max_length=250,null=True,blank=True)
    
    def __str__(self) :
        return self.name
class Advocate(models.Model):
    company=models.ForeignKey(Company, on_delete=models.SET_NULL,null=True) #on delete set null indicates that even if company is gone this advocate won't be gone 
    username=models.CharField(max_length=100)
    bio=models.TextField(max_length=250,null=True,blank=True)#It will accept null values and can be left blank
    
    def __str__(self) :
        return self.username #default way how it should appear in table [in /admin ]
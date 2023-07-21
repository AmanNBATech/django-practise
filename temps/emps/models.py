from django.db import models

# Create your models here.

class Branch(models.Model):
    branch = models.CharField(max_length=222)

    def __str__(self):
        return self.branch
    

class Student(models.Model):
    name = models.CharField(max_length=222)
    age = models.PositiveIntegerField()
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    


class Blog(models.Model):
    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.TextField()
    

from django.db import models

# Create your models here.
class education(models.Model):
    pri_school=models.TextField(max_length=45)
    middle=models.TextField(max_length=45)
    senior=models.TextField(max_length=45)
    college=models.TextField(max_length=45)

class student(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True, blank=True ,null=True)
    school = models.CharField(max_length=222,null=True)
    std = models.CharField(max_length=222)
    area = models.CharField(max_length=223,null=True)


    def __str__(self):
        return self.name
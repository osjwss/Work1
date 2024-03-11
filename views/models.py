from django.db import models

# Create your models here.
class user(models.Model):
    user = models.Model CharField (max_leght=100)
    course = models.Model CharField(max_leght=100)

class course(models.Model):
    first course = models.Model OneToOne(course)
    name = models.Model OneToOne(user,max_leght=100)
    
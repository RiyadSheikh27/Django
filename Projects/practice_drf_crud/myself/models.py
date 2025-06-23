from django.db import models

class MySelf(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)
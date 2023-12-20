from django.db import models

class Member(models.Model):
    firstname_fa = models.TextField(max_length=30)
    firstname_en = models.TextField(max_length=30)
    lastname_fa = models.TextField(max_length=30)
    lastname_en = models.TextField(max_length=30)
    position = models.TextField(max_length=30)
    profile_image = models.ImageField(upload_to='profiles/')

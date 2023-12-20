from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    date = models.DateField(auto_now=True)


class Receipt(models.Model):
    summary = models.TextField(max_length=256)
    event = models.ForeignKey(to='financial.Event', on_delete=models.CASCADE)
    amount = models.IntegerField(help_text='with Toman units')
    owner = models.CharField(max_length=32)
    date = models.DateField(auto_now=True)
    settled = models.BooleanField(default=False)
    image = models.ImageField(upload_to='receipts/', null=True)

from django.db import models
from django.utils import timezone

class Product(models.Model):
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Ticket(models.Model):

    TYPE_CHOICES = (('Bug', 'Bug'), ('Feature', 'Feature'))
    STATUS_CHOICES = (('Todo', 'ToDo'), ('Doing', 'Doing'), ('Done', 'Done'))

    type = models.CharField(max_length=7, choices=TYPE_CHOICES,
                                      default='Bug')
    issue_name = models.CharField(max_length=30, default='')
    description = models.TextField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES,
                              default="ToDo")
    urgent = models.BooleanField()
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.issue_name

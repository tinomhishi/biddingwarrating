from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ItemSale(models.Model):
    title = models.CharField(max_length=100)
    buyer = models.ForeignKey(User, related_name='buyer')
    seller = models.ForeignKey(User, related_name='seller')
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


class UserReview(models.Model):
    RATING_CHOICES = ((0, '0'),
                      (1, '*'),
                      (2, '**'),
                      (3, '***'),
                      (4, '****'),
                      (5, '*****')
                    )
    itemsale = models.ForeignKey(ItemSale)
    user = models.ForeignKey(User)
    is_buyer = models.BooleanField(default=True)
    rating = models.IntegerField(default=0, choices=RATING_CHOICES)
    review = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
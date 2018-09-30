from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models.exhibition import Exhibition


class User(AbstractUser):
    CHOICE_GENDER = (
        ('m', '남성'),
        ('f', '여성'),
        ('x', '선택안함')
    )
    profile_image = models.ImageField(upload_to='user', blank=True)
    first_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=CHOICE_GENDER)
    phone_number = models.IntegerField(default=0)
    address = models.TextField(blank=True)
    wishlist = models.ForeignKey(
        Exhibition,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.username}'

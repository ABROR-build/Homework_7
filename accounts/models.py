from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    age = models.IntegerField(default=18)
    bio = models.CharField(max_length=300)
    profile_picture = models.ImageField(
        upload_to='profile_images/',
        blank=True, null=True,
        default='deault_images/user.png'
    )
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Accounts'

    def __str__(self):
        return self.username

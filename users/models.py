from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Пользователь {self.username}: {self.first_name} {self.last_name}'

    def safe_delete(self):
        self.is_active = False
        self.save()

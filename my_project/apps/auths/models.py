from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class Client(AbstractBaseUser, PermissionsMixin):
    """
    Custom user
    """
    email = models.EmailField(
        'Почта', unique=True
    )
    
    is_active = models.BooleanField(
        'Активность', default=True
    )

    is_staff = models.BooleanField(
        'Менеджер', default=False
    )

    date_joined = models.DateTimeField(
        'Дата регистрации', default=timezone.now()
    )

    balance = models.FloatField(
        'Балланс', default=0.0
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = (
            'date_joined'
        )
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

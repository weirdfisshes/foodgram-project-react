from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Пользователь.'''
    username = models.CharField(
        'Логин',
        max_length=100,
        unique=True,
    )
    email = models.EmailField(
        'Email',
        unique=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=100
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=100
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    '''Подписка.'''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique follow',
            )
        ]

    def __str__(self):
        return self.author.username

from django.db import models
from users.models import User


class Ingredient(models.Model):
    """Ингридиент"""
    name = models.CharField(
        'Название ингридиента',
        max_length=100,
    )
    quantity = models.CharField(
        'Количество',
        max_length=100,
    )

    unit = models.CharField(
        'Единица измерения',
        max_length=100,
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.name

class Tag(models.Model):
    """Тег"""
    name = models.CharField(
        'Название тега',
        max_length=100,
        unique=True,
    )
    color = models.CharField(
        'Цветовой HEX-код',
        max_length=7,
        unique=True,
    )
    slug = models.SlugField(
        'Slug',
        max_length=100,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.slug

class Recipe(models.Model):
    """Рецепт"""
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='ingredients',
        verbose_name='Ингредиенты'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='Картинка')
    text = models.TextField(
        verbose_name='Текст рецепта'
    )
    time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления'
    )
    

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Избранное"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites_user',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique favorite')
        ]

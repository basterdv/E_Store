from django.apps import AppConfig


class CartsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "carts"
    verbose_name = 'Корзины'
    verbose_name_plural = 'Корзина'

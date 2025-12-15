from django.apps import AppConfig

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'  # ⬅️ Это критически важно! Должно быть 'pages', а не 'pages.apps' или что-то другое.
    verbose_name = 'Статические страницы'  # Это опционально
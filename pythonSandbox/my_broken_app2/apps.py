from django.apps import AppConfig


class MyBrokenApp2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_broken_app2'

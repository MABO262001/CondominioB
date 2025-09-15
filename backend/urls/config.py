# backend/urls/config.py
from django.urls import path

class Route:
    def __init__(self, prefix='', name='', controller=None):
        self.prefix = prefix
        self.name_prefix = name
        self.controller = controller

    def group(self, routes):
        urlpatterns = []
        for url, func, name in routes:
            view = getattr(self.controller, func)
            urlpatterns.append(
                path(f'{self.prefix}{url}', view, name=f'{self.name_prefix}{name}')
            )
        return urlpatterns

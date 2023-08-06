from django.conf import settings

from .default_settings import default_settings


class PFXSettings:
    def __getattr__(self, attr):
        try:
            return getattr(settings, attr)
        except AttributeError:
            return default_settings[attr]

from django.core.cache import cache

from kfsd.apps.core.services.gateway.core import Core


class Config(Core):
    def __init__(self, request=None):
        Core.__init__(self, request)

    def genCommonConfig(self):
        cache_key = "common_config"
        data = cache.get(cache_key)
        if data is None:
            payload = {"overrides": self.getDjangoRequest().getRequest().config}
            data = self.getCommonConfig(payload)
            cache.set(cache_key, data, timeout=3600)
        return data

from kfsd.apps.core.common.configuration import KubefacetsConfig
from kfsd.apps.core.auth.api.config import Config


class KubefacetsConfigMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # tmp assignment to local config
        request.config = KubefacetsConfig().genConfig()
        configHandler = Config(request)
        # actual config value assignment
        request.config = configHandler.genCommonConfig()
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        return None

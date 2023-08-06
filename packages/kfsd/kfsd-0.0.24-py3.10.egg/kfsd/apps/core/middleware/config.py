from kfsd.apps.core.common.configuration import KubefacetsConfig


class KubefacetsConfigMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.__config = KubefacetsConfig().genConfig()

    def getConfig(self):
        return self.__config

    def __call__(self, request):
        request.config = self.__config
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        return None

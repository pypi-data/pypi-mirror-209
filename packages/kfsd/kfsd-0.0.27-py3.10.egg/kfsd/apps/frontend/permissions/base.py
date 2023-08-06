from kfsd.apps.core.utils.http.base import HTTP
from kfsd.apps.core.utils.http.django.request import DjangoRequest


class BasePermission(HTTP):
    def __init__(self, request):
        self.__request = DjangoRequest(request)
        HTTP.__init__(self)

    def getDjangoRequest(self):
        return self.__request

    def getUser(self):
        return self.getDjangoRequest().getRequest().token_user

    def getCurrentRequestUrl(self):
        return self.getDjangoRequest().getRequest().build_absolute_uri()

from rest_framework import status
from kfsd.apps.core.auth.api.gateway import APIGateway


class Core(APIGateway):
    def __init__(self, request=None):
        APIGateway.__init__(self, request)

    def getCommonConfigUrl(self):
        return self.constructUrl(
            ["services.gateway.host", "services.gateway.core.common_config_uri"]
        )

    def getCommonConfig(self, payload):
        return self.httpPost(self.getCommonConfigUrl(), payload, status.HTTP_200_OK)

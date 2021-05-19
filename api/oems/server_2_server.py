from api import BaseApi


class Server2ServerApi(BaseApi):

    __resource__ = "/server2server/ad.json?"
    
    def __init__(self):
        super(Server2ServerApi, self).__init__(self.__resource__)

    def get_resource_name(self):
        return self.__resource__.split('?')[0]

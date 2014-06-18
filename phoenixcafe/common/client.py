from cafe.engine.http.client import AutoMarshallingHTTPClient

class BasePhoenixClient(AutoMarshallingHTTPClient):
    def __init__(self):
        '''
        # Init method
        '''
        super(BasePhoenixClient,self).__init__()
        

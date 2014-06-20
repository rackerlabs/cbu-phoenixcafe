from cafe.engine.http.client import AutoMarshallingHTTPClient

class BasePhoenixClient(AutoMarshallingHTTPClient):
    '''
    * Client Objects for Cloud Backup API Calls
    '''

    def __init__(self, url, auth_token, serialize_format=None,
                 deserialize_format=None):
        '''
        # Init method
        '''
        super(BasePhoenixClient,self).__init__(serialize_format,
                                                   deserialize_format)
        self.url = url
        self.auth_token = auth_token
        self.default_headers['X-Auth-Token'] = auth_token
        self.default_headers['Content-Type'] = 'application/%s' % \
                                               self.serialize_format
        self.default_headers['Accept'] = 'application/%s' % \
                                         self.deserialize_format
        
    def get_list_all_user_agents(self, url=None, requestslib_kwargs=None):
        '''
        * This is the end point to list all of the agents for a particular user
        '''

        url = url or '$s/user/agents'

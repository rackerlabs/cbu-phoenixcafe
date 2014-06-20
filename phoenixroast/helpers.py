#!/usr/bin/python
from cloudcafe.auth.provider import AuthProvider
from cloudcafe.auth.config import UserAuthConfig, UserConfig

def get_auth_token():
    '''
    * This method is to retrieve the User Auth Token from Identity
    * The credentials will be read from a config file
    * Inputs: None
    * Returns: the Auth Token ( a string of letters and numbers)
    '''
    end_config = UserAuthConfig()

    user_config = UserConfig()
    access_data = AuthProvider.get_access_data(end_config, user_config)

    return  access_data.token.id_



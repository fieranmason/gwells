import os
from urllib.parse import urlparse, urlunparse

class URLBuilder():

    def __init__(self):
        self.__AUTH_SCHEME = os.getenv('AUTH_SCHEME')
        self.__AUTH_NETLOC = os.getenv('AUTH_NETLOC')

        self.__LOGIN_PATH = os.getenv('LOGIN_PATH')
        self.__LOGOUT_PATH = os.getenv('LOGOUT_PATH')

        self.__PUBLIC_SCHEME = os.getenv('PUBLIC_SCHEME')
        self.__PUBLIC_NETLOC = os.getenv('PUBLIC_NETLOC')
        self.__PUBLIC_HOME_PATH = os.getenv('PUBLIC_HOME_PATH')
        self.__AUTH_REALMS_GWELLS = os.getenv('AUTH_REALMS_GWELLS')

        self.CLIENT_ID = os.getenv('CLIENT_ID')

        self.HOME_URI = str(self.__build_home_uri())
        self.LOGIN_URI = str(self.__build_login_uri())
        self.LOGOUT_URI = str(self.__build_logout_uri())
        self.AUTH_URI = str(self.__build_auth_uri())
        self.PUBLIC_URI = str(self.__build_public_uri())
    def __build_home_uri(self):
        #SCHEME, NETLOG, PATH, PARAMS, QUERY, FRAMGMENT
        parts = (self.__PUBLIC_SCHEME, self.__PUBLIC_NETLOC, self.__PUBLIC_HOME_PATH, '', '', '')
        return self.__build_uri('home_uri', parts)

    def __build_login_uri(self):
        query_element1='client_id=' + self.CLIENT_ID
        query_element2='response_type=code'
        query_element3='redirect_uri=' + self.HOME_URI
        query_components = [query_element1, query_element2, query_element3]

        auth_query = '&'.join(query_components)

        #SCHEME, NETLOG, PATH, PARAMS, QUERY, FRAMGMENT
        parts = (self.__AUTH_SCHEME, self.__AUTH_NETLOC, self.__LOGIN_PATH, '', auth_query, '')
        return self.__build_uri('login_uri', parts)

    def __build_logout_uri(self):
        logout_query='redirect_uri=' + self.HOME_URI

        #SCHEME, NETLOG, PATH, PARAMS, QUERY, FRAMGMENT
        parts = (self.__AUTH_SCHEME, self.__AUTH_NETLOC, self.__LOGOUT_PATH, '', logout_query, '')
        return self.__build_uri('logout_uri', parts)

    def __build_auth_uri(self):
        #SCHEME, NETLOG, PATH, PARAMS, QUERY, FRAMGMENT
        parts = (self.__AUTH_SCHEME, self.__AUTH_NETLOC + '/' + self.__AUTH_REALMS_GWELLS, '', '', '', '')
        return self.__build_uri('auth_uri', parts)

    def __build_public_uri(self):
        #SCHEME, NETLOG, PATH, PARAMS, QUERY, FRAMGMENT
        parts = (self.__PUBLIC_SCHEME, self.__PUBLIC_NETLOC, '', '', '', '')
        return self.__build_uri('public_uri', parts)

    def __build_uri(self, name, parts):
        uri = urlunparse(parts)
        print(name, ': ', uri)
        return uri

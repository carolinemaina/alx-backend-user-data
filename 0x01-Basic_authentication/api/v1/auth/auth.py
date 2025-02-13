#!/usr/bin/env python3
'''
file auth.py
'''
from typing import List, TypeVar, Optional
from flask import Flask, request


class Auth:
    ''' A Class to manage the API authentication.
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Required auth
        '''
        if path and not path.endswith('/'):
            path = path + '/'

        if not path or path not in excluded_paths:
            return True

        if not excluded_paths or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False
        return False


    def authorization_header(self, request=None) -> Optional[str]:
        '''
        Returns the value of the Authorization header or None
        '''
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')


    def current_user(self, request=None) -> None:
        '''TypeVar('User'):
         Current User
        request = Flask(__name__)'''
        return

if __name__ == '__main__':
    a = Auth()

    print(a.require_auth(None, None))
    print(a.require_auth(None, []))
    print(a.require_auth("/api/v1/status/", []))
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))

#!/usr/bin/env python3
"""
handle session authentication
"""
import uuid
from typing import TypeVar, Optional
from models.user import User
from api.v1.auth.auth import Auth
from flask import request


class SessionAuth(Auth):
    """
    class that handles session auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id for the user.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user id of the user associated with
        a given session id.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> Optional[User]:
        """
	    Returns the User instance based on a session cookie
	    """
        if request is None:
            return None
        
        session_id = request.cookies.get(self.session_cookie())
        
        if session_id is None:
            return None
        
        user_id = self.user_id_for_session_id(session_id)
        
        if user_id is None:
            return None
        
        user = User.get(user_id)
        return user

    def session_cookie(self):
        """
	    Returns the cookie name for the session (e.g., '_my_session_id')
	    """
        return "_my_session_id"

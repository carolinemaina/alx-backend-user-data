#!/usr/bin/env python3
"""
handle session auth
"""
import base64 import b64decode
import uuid import uuid4
from typing import Optional, Tuple, TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    class that handles session auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> Optional[str]:
        """Creates a session id for the user.
        """
        if not user_id or not isinstance(user_id, str):
            return
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the user id of the user associated with
        a given session id.
        """
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

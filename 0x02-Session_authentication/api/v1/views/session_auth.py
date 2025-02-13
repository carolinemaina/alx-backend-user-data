#!/usr/bin/env python3
"""Module of session authenticating views.
"""
import os
from typing import Tuple
from flask import abort, jsonify, request
from models.user import User
from api.v1.views import app_views
from werkzeug.exceptions import BadRequest


@app_views.route('/api/v1/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handle user login for session authentication.
    """
    # Step 1: Retrieve email and password from request.form
    email = request.form.get('email')
    password = request.form.get('password')

    # Step 2: Check if email or password is missing
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Step 3: Retrieve the user based on email
    user = User.search(email)
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    # Step 4: Check if the password is correct
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Step 5: Create a session ID for the user
    session_id = auth.create_session(user.id)

    # Step 6: Return the user information and set the session ID as a cookie
    response = jsonify(user.to_json())
    response.set_cookie(auth.session_cookie(), session_id)
    return response

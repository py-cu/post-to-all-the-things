import os, codecs
from functools import wraps
from flask import request, redirect, url_for

import database
from web.models import User, Session

COOKIE_ID = 'pt_id'
SESSION_KEY_LENGTH = 30

db = database.get_session()

def authenticate_user(username, password):
    user = db.query(User).filter_by(name=username).first()
    if not user:
        raise AuthenticationException("No user found")
    if not user.check_password(password):
        raise AuthenticationException("Password mismatch")

    return user

def create_session(user, response):
    key = codecs.encode(os.urandom(SESSION_KEY_LENGTH), "hex").decode()
    user_session = Session(user=user, key=key)
    db.add(user_session)
    db.commit()
    response.set_cookie(COOKIE_ID, key)

def require_login(view):
    @wraps(view)
    def check_login():
        session_key = request.cookies.get(COOKIE_ID)
        if session_key:
            session = db.query(Session).filter_by(key=session_key).first()
            if session:
                return view()
        # make it this far, auth failed
        return redirect(url_for('login'))
    
    return check_login


class AuthenticationException(Exception):
    pass

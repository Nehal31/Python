
from flask import session
from functools import wraps

def checker_logged_in(func):
    @wraps(func) 
    def wraper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in'
    return wraper
        

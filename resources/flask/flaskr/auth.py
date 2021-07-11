#!/usr/bin/env python3

from flask import Blueprint, jsonify, request
from flaskr.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() if request.get_json() is not None else {}
    name = data.get('name', None)
    username = data.get('username', None)
    password = data.get('password', None)

    db = get_db()
    error = None

    if not name:
        error = 'Name is required.'
    elif not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    elif db.execute('SELECT id FROM user WHERE username = ?', (username,)).fetchone() is not None:
        error = f'Username {username} is taken.'

    if error is not None:
        return jsonify({error: error})

    db.execute('INSERT INTO user (name, username, password) VALUES (?, ?, ?)', (name, username, generate_password_hash(password)))
    db.commit()
    return jsonify({})
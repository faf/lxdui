from flask import Blueprint, session, jsonify
from flask_jwt import jwt_required

from app.lib.remote import Remote

from app.api.models.LXDModule import LXDModule
from app.api.utils import response

remote_api = Blueprint('remote_api', __name__)

@remote_api.route('/')
@jwt_required()
def remote():
    try:
        remotes = [{'name': x['name'], 'selected': session['host'] is not None and i == session['host'] } for i, x in enumerate(Remote().get_list())]
        return jsonify({'status': 200, 'message': 'ok', 'data': remotes})
    except ValueError as e:
        return response.replyFailed(message=e.__str__())

from flask import jsonify, request
from flask_pluginengine import current_plugin
from werkzeug.exceptions import Forbidden

from indico.web.rh import RH
from indico.modules.users.util import get_user_by_email
from indico.modules.events.util import get_events_managed_by, get_events_with_linked_event_persons

class RHGetEventsByEmail(RH):
    """Export events managed by or linked to a specific user identified by email"""

    def _process(self):
        token = request.headers.get('Authorization')
        expected_token = current_plugin.settings.get('token')
        if not expected_token or not token or token != expected_token:
            raise Forbidden
        email = request.view_args['email']
        user = get_user_by_email(email)
        if user is None:
            raise Forbidden
        managed_events = get_events_managed_by(user)
        linked_events = get_events_with_linked_event_persons(user)
        return jsonify(user_id=user.id, managed_events=list(managed_events), linked_events=list(linked_events))

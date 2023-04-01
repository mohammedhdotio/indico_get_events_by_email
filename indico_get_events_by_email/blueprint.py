from indico.core.plugins import IndicoPluginBlueprint

from indico_get_events_by_email.controllers import RHGetEventsByEmail


blueprint = IndicoPluginBlueprint('indico_get_events_by_email', __name__)
blueprint.add_url_rule('/get_events_by_email/<email>', 'get_events_by_email', RHGetEventsByEmail, methods=('GET',))

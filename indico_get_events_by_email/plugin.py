from wtforms.fields import StringField, URLField
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint, url_for_plugin
from indico.web.forms.base import IndicoForm
from indico_get_events_by_email.blueprint import blueprint
from indico_get_events_by_email import _
from wtforms.validators import DataRequired

class SettingsForm(IndicoForm):
    token = StringField(_('Token'), [DataRequired()],
                          description=_('The API token to access the <tt>this plugin</tt> service'))


class GetEventsByEmailPlugin(IndicoPlugin):
    """Get Events By Email

    A plugin to export events ids managed/linked by/to email address .
    """
    configurable = True
    settings_form = SettingsForm
    default_settings = {
        'token': 'GsxaEHcRZcLEekG711REQiSOCF4kAVdH'
    }
    friendly_name = "Get managed/linked events by email address"

    def get_blueprints(self):
        return blueprint

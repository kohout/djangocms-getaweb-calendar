from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import EventCalendarPluginModel, Event

class EventCalendarPlugin(CMSPluginBase):
    model = EventCalendarPluginModel
    name = _("Calendar")
    render_template = "cms/plugins/calendar/view.html"

    def get_events(self, instance):
        q = Event.objects.all()
        #if instance.view_mode == 'TEASER':
        #    pass
        #    #q = q[:5]
        #if instance.view_mode in  ['CALENDAR', 'LIST_AND_CALENDAR']:
        #    self.request.GET.get('month', 0)
        return q

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['events'] = list(self.get_events(instance))
        context['categories'] = list(set(
            [e.category for e in context['events']]))
        return context

plugin_pool.register_plugin(EventCalendarPlugin)

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from colors.fields import ColorField
import mptt
import settings

class EventCategory(models.Model):
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True)
    name = models.CharField(
        max_length=30,
        verbose_name=_(u'Category Name'))
    color = ColorField(
        default='FF0000',
        verbose_name=_(u'Color'))

    def color_mark(self):
        raw_html = u'<div class="color-mark" style="width: 16px; height: 16px; background: #%s"></div>'
        return raw_html % self.color

    color_mark.allow_tags = True
    color_mark.short_description = _(u'Color')


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cmscalendar-category', args=[self.pk])

try:
    mptt.register(EventCategory)
except mptt.AlreadyRegistered:
    pass


class EventCalendarPluginModel(CMSPlugin):
    VIEW_MODES = (
        ('TEASER', _(u'Teaser View')),
        ('LIST', _(u'List-View')),
        ('CALENDAR', _(u'Calendar-View')),
        ('LIST_AND_CALENDAR', _(u'List- and Calendar-View')),
    )

    title = models.CharField(
        max_length=150,
        verbose_name=_(u'Headline of the calender view'))
    selected_categories = models.ManyToManyField(
        EventCategory,
        verbose_name=_(u'Selected Categories'))
    view_mode = models.CharField(
        max_length=20,
        choices=VIEW_MODES,
        verbose_name=_(u'View Mode'))

    def copy_relations(self, old_instance):
        self.selected_categories = old_instance.selected_categories.all()

    class Meta:
        verbose_name = _(u'Calendar Plugin')
        verbose_name_plural = _(u'Calendar Plugins')


class Event(models.Model):
    start_date = models.DateField(
        verbose_name=_(u'Start Date'))
    start_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=_(u'Start Time'))
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_(u'End Date'))
    end_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=_(u'End Time'))
    title = models.CharField(
        max_length=255,
        verbose_name=_(u'Title'))
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_(u'Description'))
    category = models.ForeignKey(
        EventCategory,
        blank=True,
        null=True,
        verbose_name=_(u'Event Category'))

    @property
    def color(self):
        return u'#%s' % self.category.color

    @property
    def text_color(self):
        return u'#FFFFFF'

    @property
    def start(self):
        return self.start_date

    def complete_datetime(self):
        if self.end_date:
            _date = u'%s bis %s' % (
                self.start_date.strftime('%d.%m.'),
                self.end_date.strftime('%d.%m.')
            )
        else:
            _date = self.start_date.strftime('%d.%m.')

        _time = []
        if self.start_time:
            _time.append(self.start_time.strftime('%H:%M'))
        if self.end_time:
            _time.append(self.end_time.strftime('%H:%M'))

        _time = u' - '.join(_time)
        return u'%s, %s' % (_date, _time)

    class Meta:
        ordering = ('start_date', 'start_time', )
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

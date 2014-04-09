from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import EventCategory, Event

class EventCategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'color_mark', )

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'start_time',
        'end_date', 'end_time', 'category', )
    fields = (
        ('start_date', 'start_time', ),
        ('end_date', 'end_time', ),
        ('title', 'category', ),
        ('description', ),
    )

admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(Event, EventAdmin)

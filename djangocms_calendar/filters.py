# -*- coding: utf-8 -*-
import django_filters
from .models import Event


class EventFilter(django_filters.FilterSet):
    start = django_filters.DateFilter(name='start_date', lookup_type='gte')
    end = django_filters.DateFilter(name='end_date', lookup_type='lte')

    class Meta:
        model = Event
        fields = ['start', 'end']

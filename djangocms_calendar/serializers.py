# -*- coding: utf-8 -*-
from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    start = serializers.Field()
    color = serializers.Field(source='color')
    textColor = serializers.Field(source='text_color')
    complete_datetime = serializers.Field()

    class Meta:
        model = Event
        fields = ('id', 'url', 'title', 'description',
            'color', 'textColor', 'complete_datetime',
            'start', 'start_date', 'start_time',
            'end_date', 'end_time', )

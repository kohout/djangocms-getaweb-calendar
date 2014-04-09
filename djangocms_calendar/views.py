# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from .filters import EventFilter

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for event items
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_class = EventFilter

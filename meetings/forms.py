from django.forms import modelform_factory

from meetings.models import Meeting

MeetingForm = modelform_factory(Meeting, exclude=[])

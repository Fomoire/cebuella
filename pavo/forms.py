from django import forms
from django.utils.safestring import mark_safe

class EventSplitDateTime(forms.SplitDateTimeWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(attrs={'class': 'vDateField'}), 
                   forms.TextInput(attrs={'class': 'vTimeField'})]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

    def format_output(self, rendered_widgets):
        return mark_safe(u'%s<br />%s' % (rendered_widgets[0], rendered_widgets[1]))


class NewsTab(forms.Form):
    fro = forms.DateTimeField(widget=EventSplitDateTime())
    to = forms.DateTimeField(widget=EventSplitDateTime())

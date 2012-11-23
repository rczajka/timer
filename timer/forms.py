from datetime import datetime
from time import mktime
from django import forms
from .models import Timer

class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer

    def __init__(self, data=None, instance=None, *args, **kwargs):
        if instance is not None:
            self.old_minutes = instance.minutes
            self.old_seconds = instance.seconds
            self.old_time = self.old_minutes * 60 + self.old_seconds
            self.old_state = instance.state
        super(TimerForm, self).__init__(data=data, instance=instance, *args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        instance = super(TimerForm, self).save(commit=False, *args, **kwargs)
        stamp = mktime(datetime.now().timetuple())
        if (hasattr(self, 'old_state') and
                self.old_state in ('start', 'resume') and
                instance.state == 'pause' and
                instance.change_stamp):
            new_time = self.old_time - (stamp - instance.change_stamp)
            instance.minutes = new_time / 60
            instance.seconds = new_time % 60
        instance.change_stamp = stamp
        instance.save()
        return instance

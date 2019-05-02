from django import forms

from jobsapp.models import Job, Applicant
from accounts.models import Message



class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'created_at',)

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)



class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('Name', 'Message',)

    def is_valid(self):
        valid = super(CreateMessageForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        Message = super(CreateMessageForm, self).save(commit=False)
        if commit:
            Message.save()
        return Message
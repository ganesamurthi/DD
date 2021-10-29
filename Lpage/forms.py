from django import forms

from Lpage.models import Subscriber

class SubscriberEntryForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email','mobile']

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     return email

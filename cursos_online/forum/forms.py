from django import forms

from .models import Reply


class Replyform(forms.ModelForm):
    
    class Meta:
        model = Reply
        fields = ['reply']
from django import forms
from .models import Quote, Comment


class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = [
            'name',
            'description',
            'image',
            ]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
            ]

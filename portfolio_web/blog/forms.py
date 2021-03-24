from django import forms
from .models import Post

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class postForm(forms.Form):
    class Meta:
        model = Post
        fields = '_all_' #('title', 'body', 'categories')
        #category_choices = (("Django", "Django"),("Python", "Python"),)

        #widgets = {
        #    'title': forms.TextInput(attrs={'class': 'form-control'}),
        #    'body': forms.Textarea(attrs={'class': 'form-control'}),
        #    'categories': forms.ChoiceField(choices = category_choices),
        #}
from .models import NewPost

from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = '__all__'
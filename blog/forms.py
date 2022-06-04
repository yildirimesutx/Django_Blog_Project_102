from .models import NewPost, Comments

from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        # fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comments
        # fields = '__all__'       
        exclude = ('post',)
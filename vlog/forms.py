from django.forms import ModelForm
from .models import *
from django import forms


class TzUserForm(ModelForm):
    confirm_pass = forms.CharField(max_length=100)

    class Meta:
        model = TzUser
        fields = ('username', 'photo', 'email', 'password', 'confirm_pass', 'phone_number')

    def clean(self):
        clean_data = super().clean()
        if clean_data.get('password') != clean_data.get('confirm_pass'):
            raise forms.ValidationError('Passwords are not equal!')


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'picture')


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)

from django import forms
from django.contrib.auth import get_user_model
from .models import Comment
from .models import Post


User = get_user_model()


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'datetime-local'},
                                        format='%Y-%m-%dT%H:%M'),
        }
        exclude = ('author',)

from django import forms
from .models import Post
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'password')
        labels={
            'username': '아이디',
            'password': '비밀번호'
            
        }
        widgets={
            'password': forms.PasswordInput()
        }
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents')


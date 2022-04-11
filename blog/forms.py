from .models import BlogPost, Tag
from django import forms


choices = Tag.objects.all().values_list("tag_name", "tag_name")

choices_list = []
for item in choices:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'title_tag', 'author', 'tag', 'text', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Title"}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'tag': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'title_tag', 'text', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

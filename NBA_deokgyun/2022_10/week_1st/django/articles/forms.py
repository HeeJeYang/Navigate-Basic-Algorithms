from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력해줘',
            }   
        )
    )

    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용도 입력해줘',
            }
        ),
    )

    class Meta:
        model = Article
        fields = '__all__'
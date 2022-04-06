from django import forms
from .models import Article

"""
Form 의 역할
1. 유효성검사(Validation)
2. HTML 생성

ModelForm의 역할
3. DB 연동(저장까지)
""" 

class ArticleForm(forms.ModelForm):
    
    title = forms.CharField(min_length=2, max_length=10)

    class Meta:
        model = Article
        fields = ('title', 'content',)

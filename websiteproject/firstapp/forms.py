from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title','content', 'category', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 20}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }
    def clean_title(self):
        title =self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Нужно вести текст!')
        return title


    # title = forms.CharField(max_length=150, label='Название новости ',
    #                         widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='Текст ', required=False,
    #                           widget=forms.Textarea(attrs={"class": "form-control",
    #                                                        "rows": 20})  )
    # is_published = forms.BooleanField(label='Опубликовано? ', initial=True)
    # category = forms.ModelChoiceField(empty_label='Выберите новость',label='Категория ',
    #                                   queryset = Category.objects.all(),
    #                                   widget=forms.Select(attrs={"class": "form-control"}))





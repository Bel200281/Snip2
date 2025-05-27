from django.forms import ModelForm
from MainApp.models import Snippet
from django.core.exceptions import ValidationError




class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']
    


def clean_name(self):
    """"Метод для проверки длины поля <name>"""
    snippet_name = self.cleaned_data.get('name')
    if snippet_name is None or len(snippet_name.strip()) < 3:
        raise ValidationError ("Название должно быть минимум 4 символа.")
    return snippet_name


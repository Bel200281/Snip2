from django.forms import ModelForm, Textarea, TextInput
from MainApp.models import Snippet
from django.core.exceptions import ValidationError




class SnippetForm(ModelForm):
       class Meta:
             model = Snippet
             # Описываем поля, которые будем заполнять в форме
             fields = ['name', 'lang', 'code']
             labels = {"name": "", "lang": "", "code": ""}
             widgets = {
                    "name": TextInput(attrs={
                           "class": "form-control",
                           "placeholder": "Название сниппета",
                           "style": "max-width: 300px"

                     }),
                     "code": Textarea(attrs={
                    "placeholder": "Код сниппета",
                    "rows": 5,
                    "class": "input-large",
                    "style": "width: 50% !important; resize: vertical !important;"
                     }),
             }
                          


       def clean_name(self):
              """"Метод для проверки длины поля <name>"""
              snippet_name = self.cleaned_data.get('name')
              if snippet_name is None or len(snippet_name.strip()) < 3:
                      raise ValidationError ("Название должно быть минимум 4 символа.")
              return snippet_name
       



from django.db import models

LANGS = (
    ("py", "Python"),
    ("js", "JavaScript"),
    ("go", "Golang"),
    ("cpp", "C++"),
    ("html", "HTML")
)

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)

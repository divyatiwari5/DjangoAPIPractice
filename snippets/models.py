from django.db import models


# Create your models here.


LANGUAGE_CHOICES = [('PY', 'Python'),
                    ('J', 'JAVA'),
                    ('C', 'C')]
STYLE_CHOICE = [('C', 'Cursive'),
                ('I', 'Italic')]

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True, default='')
    code = models.TextField()
    boolean = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='Node', max_length=20)
    style = models.CharField(choices=STYLE_CHOICE, default='STYLE', max_length=50)

    class Meta:
        ordering = ('created',)
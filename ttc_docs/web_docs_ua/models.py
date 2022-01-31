from django.db import models
from django.utils import timezone


class CategoryUa(models.Model):

    WANT = 'want'
    ALREADY = 'already'

    CHOICES = (
        (WANT, 'want'),
        (ALREADY, 'already')
    )

    category = models.CharField(max_length=50, verbose_name='category')
    chapter = models.CharField(max_length=20, choices=CHOICES, verbose_name='capture')
    place = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.category}'

    def __repr__(self):
        return f'{self.category}'


class ArticleUa(models.Model):

    category = models.ForeignKey(CategoryUa, on_delete=models.DO_NOTHING, verbose_name='category')
    title = models.CharField(max_length=100, verbose_name='title')
    preview = models.TextField(max_length=200, verbose_name='preview', blank=True)
    paragraph1 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph2 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph3 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph4 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph5 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph6 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph7 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph8 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph9 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    paragraph10 = models.TextField(max_length=9999, verbose_name='article text', blank=True)
    advise = models.ForeignKey('AdvisesUa', on_delete=models.DO_NOTHING, verbose_name='advise', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = '-date',

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title} | {self.date}'


class AdvisesUa(models.Model):

    preview = models.TextField(max_length=200, verbose_name='preview')
    text = models.TextField(max_length=9999, verbose_name='advise text', null=True)

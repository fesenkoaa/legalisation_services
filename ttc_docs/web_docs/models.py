from django.db import models
from django.utils import timezone


class Category(models.Model):

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


class Article(models.Model):

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='category')
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
    advise = models.ForeignKey('Advises', on_delete=models.DO_NOTHING, verbose_name='advise', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = '-date',

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title} | {self.date}'


class Reviews(models.Model):

    email = models.EmailField(blank=True)
    auth = models.CharField(max_length=50, blank=False)
    message = models.CharField(max_length=500, blank=False)
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = '-time',
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.auth} add a new comment'


class Messages(models.Model):

    email = models.EmailField(blank=True)
    auth = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=500, blank=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = '-date',
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.auth} sent a message'


class Contact(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='Name')
    phone = models.BigIntegerField(verbose_name='Phone')
    message = models.TextField(verbose_name='Message')
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.phone}"


class Advises(models.Model):

    preview = models.TextField(max_length=200, verbose_name='preview')
    text = models.TextField(max_length=9999, verbose_name='advise text', null=True)


class AppImage(models.Model):

    title = models.CharField(max_length=100, verbose_name='title', blank=True, null=True)
    images = models.ImageField(verbose_name='image')


class ServiceCategory(models.Model):

    category = models.CharField(max_length=30, verbose_name='category')

    def __str__(self):
        return f'{self.category}'

    def __repr__(self):
        return f'{self.category}'


class Services(models.Model):

    category = models.ForeignKey(ServiceCategory, on_delete=models.DO_NOTHING, verbose_name='category')
    service_name = models.CharField(max_length=50, verbose_name='service name')
    service_name_ua = models.CharField(max_length=50, verbose_name='service name ua', blank=True)

    def __str__(self):
        return f'{self.category} {self.service_name}'

    def __repr__(self):
        return f'{self.category} {self.service_name}'


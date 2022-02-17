import datetime
from django.db import models
from hashlib import md5
from django.utils import timezone
from django.urls import reverse


class URL(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название сайта')
    full_url = models.URLField(verbose_name='Полный URL адрес')
    short_url = models.URLField(verbose_name='Короткий URL адрес', unique=True)
    pub_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    def count_views(self):
        self.views += 1
        self.save()

    def get_absolute_url(self):
        return reverse('route', kwargs={'key': self.short_url})

    def was_published_a_long_time_ago(self):
        return self.pub_data >= (timezone.now() - datetime.timedelta(days=15)).delete()

    @classmethod
    def create(self, full_url, title):
        temp_url = md5(full_url.encode()).hexdigest()[:6]
        try:
            obj = self.objects.create(short_url=temp_url, full_url=full_url, title=title)
        except TypeError:
            obj = self.objects.create(full_url=full_url, title=title)
        return obj

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'



from django.db import models



class Section(models.Model):
    section_name = models.CharField(max_length=25 , verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.section_name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tag = models.ManyToManyField(Section, through='Sectionship')
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Sectionship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='Sectionship')
    tags = models.ForeignKey(Section, on_delete=models.CASCADE)
    is_main = models.BooleanField(u'Главная')

    def __str__(self):
        return f'{self.article}_{self.tags}'
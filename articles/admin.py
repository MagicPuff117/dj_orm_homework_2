from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Section, Sectionship



class Tags_throughFormset(BaseInlineFormSet):
    def clean(self):
        tags_counter = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                tags_counter += 1
        if tags_counter == 0:
            raise ValidationError('Выберете основной раздел')
        if tags_counter > 0:
            raise ValidationError('Основной раздел уже выбран')
        return super().clean()


class Tags_throughInline(admin.TabularInline):
    model = Sectionship
    formset = Tags_throughFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [Tags_throughInline]

@admin.register(Section)
class TagsAdmin(admin.ModelAdmin):
    ordering = ['section_name']
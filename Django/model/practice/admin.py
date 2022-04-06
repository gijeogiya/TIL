from django.contrib import admin
from .models import Student, Article

admin.site.register(Student)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at',)


admin.site.register(Article, ArticleAdmin)


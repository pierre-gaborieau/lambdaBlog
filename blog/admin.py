from django.contrib import admin

from .models import Article, Paragraphe, Profile

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(Paragraphe)

from django.contrib import admin
from . models import User, NewsArticle

# Registering base models here.
admin.site.register(User)
admin.site.register(NewsArticle)
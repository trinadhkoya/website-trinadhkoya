from django.contrib import admin

# Register your models here.
from application.models import Post

admin.site.register(Post)
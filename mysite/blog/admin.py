from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Поля для редактирования (created_at убран!)
    fields = ('title', 'content')

    # Поля для отображения в списке постов (created_at можно оставить)
    list_display = ('title', 'created_at')

admin.site.register(Post, PostAdmin)
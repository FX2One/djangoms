from django.contrib import admin
from .models import Comic
# Register your models here.
class ComicsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comic, ComicsAdmin)
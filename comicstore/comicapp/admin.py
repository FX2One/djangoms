from django.contrib import admin
from .models import Comic, ComicSeries
# Register your models here.

class ComicsAdmin(admin.ModelAdmin):
    list_display = ('title','series')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comic, ComicsAdmin)
admin.site.register(ComicSeries)
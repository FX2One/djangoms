from django.contrib import admin
from .models import Comic, ComicSeries, Available
# Register your models here.

class ComicsAdmin(admin.ModelAdmin):
    list_display = ('title','series','date')
    list_filter = ('title','date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comic, ComicsAdmin)
admin.site.register(ComicSeries)
admin.site.register(Available)
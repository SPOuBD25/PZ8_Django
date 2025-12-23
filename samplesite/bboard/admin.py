from django.contrib import admin
from .models import Bb, Rubric, Sticker, BbExtra

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'content', 'price', 'published','get_stickers')
    list_filter = ('published', 'rubric','stickers')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

    def get_stickers(self, obj):
        return ", ".join([s.name for s in obj.stickers.all()])

    get_stickers.short_description = 'Метки'

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(Sticker)
admin.site.register(BbExtra)
from django.contrib import admin
from .models import Catgoriyes, News, Contact, Comment, Subjects


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]


admin.site.register(Catgoriyes)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Subjects)

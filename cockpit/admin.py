from django.contrib import admin

from cockpit.models import BiCommonPagesu, PagesuDocID
# Register your models here.
@admin.register(BiCommonPagesu)
class BiCommonPagesuAdmin(admin.ModelAdmin):
    pass
# admin.site.register(BiCommonPagesu)
@admin.register(PagesuDocID)
class PagesuDocIDAdmin(admin.ModelAdmin):
    pass
# admin.site.register(PagesuDocID)
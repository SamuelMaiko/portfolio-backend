from django.contrib import admin
from .models import SaccoAppUpdate

@admin.register(SaccoAppUpdate)
class SaccoAppUpdateAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'created_at')
    search_fields = ('version_name',)
    ordering = ('-created_at',)

from django.contrib import admin
from .models import Service, KeyFeature


class KeyFeatureInline(admin.TabularInline):
    model = KeyFeature
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'badge', 'sequence', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'badge', 'description']
    ordering = ['sequence', 'name']
    inlines = [KeyFeatureInline]


@admin.register(KeyFeature)
class KeyFeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'created_at']
    list_filter = ['service', 'created_at']
    search_fields = ['name', 'service__name']

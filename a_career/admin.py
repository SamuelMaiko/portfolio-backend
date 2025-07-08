from django.contrib import admin
from .models import Company, Career, CareerAchievement, CareerTechnology


class CareerAchievementInline(admin.TabularInline):
    model = CareerAchievement
    extra = 1


class CareerTechnologyInline(admin.TabularInline):
    model = CareerTechnology
    extra = 1


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'company_type', 'created_at']
    search_fields = ['name', 'location', 'company_type']


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'employment_type',
                    'status', 'start_date', 'end_date']
    list_filter = ['employment_type', 'status', 'company']
    search_fields = ['position', 'company__name']
    inlines = [CareerAchievementInline, CareerTechnologyInline]


@admin.register(CareerAchievement)
class CareerAchievementAdmin(admin.ModelAdmin):
    list_display = ['career', 'achievement', 'created_at']
    list_filter = ['career']
    search_fields = ['achievement', 'career__position']


@admin.register(CareerTechnology)
class CareerTechnologyAdmin(admin.ModelAdmin):
    list_display = ['technology_name', 'career', 'created_at']
    list_filter = ['career']
    search_fields = ['technology_name', 'career__position']

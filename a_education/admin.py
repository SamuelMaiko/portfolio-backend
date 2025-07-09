from django.contrib import admin
from .models import Institution, Education, EducationSkill


class EducationSkillInline(admin.TabularInline):
    model = EducationSkill
    extra = 1


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'created_at']
    search_fields = ['name', 'location']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'institution',
                    'education_type', 'status', 'start_date', 'end_date']
    list_filter = ['education_type', 'status', 'institution']
    search_fields = ['title', 'institution__name']
    inlines = [EducationSkillInline]


@admin.register(EducationSkill)
class EducationSkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'education', 'created_at']
    list_filter = ['education']
    search_fields = ['skill_name', 'education__title']

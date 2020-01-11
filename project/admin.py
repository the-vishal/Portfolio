from django.contrib import admin
from .models import Project
from django.contrib.admin.filters  import DateFieldListFilter
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	date_hierarchy = 'date'
	list_filter = (	
		('date', DateFieldListFilter),
	)
	list_display = ('name', 'date')
	search_fields = ('name', )

# admin.site.register(Project, ProjectAdmin)
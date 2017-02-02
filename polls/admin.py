from django.contrib import admin
from .models import Issue, Option

# Register your models here.
class OptionInline(admin.TabularInline):
    model = Option
    extra = 1
class IssueAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['issue_text']}),
	('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [OptionInline]
    list_display = ('issue_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['issue_text']
admin.site.register(Issue, IssueAdmin)


from django.contrib import admin
from testing.models import Load
# Register your models here.

#class ChoiceInline(admin.TabularInline):
	#model = Load
	#extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['Region','Category','SubCat']}),
	]

	list_display = ('Region', 'Category', 'SubCat')
	list_filter = ['Category','SubCat']
	search_fields = ['Region']
	#inlines = [ChoiceInline]

admin.site.register(Load,QuestionAdmin)

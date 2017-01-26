from django.contrib import admin
from testing.models import Load
import autocomplete_light
# Register your models here.

#class ChoiceInline(admin.TabularInline):
	#model = Load
	#extra = 3

class QuestionAdmin(admin.ModelAdmin):
	form = autocomplete_light.modelform_factory(Load, fields='__all__')
	fieldsets = [
		(None,               {'fields': ['Region','Category','SubCat']}),
	]
	list_display = ('Region', 'Category', 'SubCat')
	list_filter = ['Category','SubCat']
	search_fields = ['Region']
	#inlines = [ChoiceInline]

admin.site.register(Load,QuestionAdmin)

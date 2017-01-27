import autocomplete_light.shortcuts as al
from testing.models import Load

al.register(Load,
	search_fields=['Region','Category','SubCat'],
	attrs={
	'placeholder' : 'search here',
	'data-autocomplete-minimum-characters': 1,
	},

	widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },

	)
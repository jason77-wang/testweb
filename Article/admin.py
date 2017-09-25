from django.contrib import admin
from Article.models import Test
from Article.models import Tag
from Article.models import Contact
 
# Register your models here.
#admin.site.register([Test, Contact, Tag])

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
 
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]
 
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])

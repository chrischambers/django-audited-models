from django.contrib import admin


class AuditedAdmin(admin.ModelAdmin):
    raw_id_fields = ['creator', 'editor']
    readonly_fields = ('creator', 'editor', 'datetime_created', 'datetime_modified')
    date_hierarchy = "datetime_created"

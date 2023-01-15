from django.contrib import admin
from .models import Questions, Form, Choices, Answer, Responses

from django.contrib import admin

admin.site.site_header = "Collect"
admin.site.site_title = "Collect | Admin"
admin.site.index_title = "Welcome to Collect Admin Panel"

# Register your models here.
admin.site.register(Questions)
admin.site.register(Choices)
# admin.site.register(Form)
admin.site.register(Answer)
# admin.site.register(Responses)


@admin.register(Form) 
class FormAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')


@admin.register(Responses) 
class ResponsesAdmin(admin.ModelAdmin):
    list_display = ( 'responder_email', "form_name")

    def form_name(self, obj):
        return obj.form_id.title





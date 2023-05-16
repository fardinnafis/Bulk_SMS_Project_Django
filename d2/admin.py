from django.contrib import admin
from d2.models import AddPeople
from d2.models import ErrorMessage, Feedback
# Register your models here.

class AddPeopleAdmin(admin.ModelAdmin):
    list_display = ["number","senderID"]
admin.site.register(AddPeople,AddPeopleAdmin)


class ErroMessageAdmin(admin.ModelAdmin):
    list_display = ["code"]
admin.site.register(ErrorMessage,ErroMessageAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name','email']
admin.site .register(Feedback,FeedbackAdmin)


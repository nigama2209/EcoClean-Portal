from django.contrib import admin # type: ignore
from . import models

# Register your models here.
@admin.register(models.adminprofile)
class adminprofileAdmin(admin.ModelAdmin):
    list_display=["Name","EmailId","PhoneNumber"]
@admin.register(models.ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display=["Name","EmailId","PhoneNumber","Message"]
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(models.userregistration)
class userregistrationAdmin(admin.ModelAdmin):
    list_display=["Name","username","EmailId","PhoneNumber","address","userid"]
    search_fields=["userid"]  
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
@admin.register(models.addbranch)
class addbranchAdmin(admin.ModelAdmin):
    list_display=["branchname","branchId","Branchadd"]
    search_fields=["branchId"]
@admin.register(models.addservice)
class addserviceAdmin(admin.ModelAdmin):
    list_display=["servicename","typeofcloth","price"]
    search_fields=["typeofcloth"]
    list_filter=["typeofcloth"]
@admin.register(models.clothtype)
class clothtypeAdmin(admin.ModelAdmin):
    list_display=["typeofcloth"]
    search_fields=["typeofcloth"]
@admin.register(models.servicename)
class servicenameAdmin(admin.ModelAdmin):
    list_display=["servicename"]
    search_fields=["servicename"]
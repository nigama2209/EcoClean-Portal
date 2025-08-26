from django.contrib import admin # type: ignore
from . import models
# Register your models here.
@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["bookingid","username","paymentdetails","totalamount","bookingdate"]
    search_fields=["customername"]
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["bookingid","username","rating","message"]
    search_fields=["bookingid"]
    list_filter=["rating"]
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
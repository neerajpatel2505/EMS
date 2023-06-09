from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserDataBase)
admin.site.register(models.AdminDataBase)
admin.site.register(models.EnquiryDataBase)
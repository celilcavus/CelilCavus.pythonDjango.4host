from django.contrib import admin
from .models import AboutModel
# Register your models here.
class AdminAboutModel(admin.ModelAdmin):
    list_display = ('id','Title')



admin.site.register(AboutModel,AdminAboutModel)
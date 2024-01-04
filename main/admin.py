from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'pub_1_check', 'pub_2_check', 'pub_3_check', 'pub_3_check', 'cv_check', 'pub_4_check', 'pub_5_check', 'aps_check', 'pub_6_check', 'pre_synopsis_check', 'pub_7_check', 'thesis_check', 'pdc_check')

admin.site.register(User, UserAdmin)

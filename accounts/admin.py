from django.contrib import admin
from .models import Profile, create_user_profile, save_user_profile

# Register your models here.
admin.site.site_header = "WorkFlow Admin"
admin.site.site_title = "WorkFlow"



class ProfileAdmin(admin.ModelAdmin):
    list_display =('location','bio','birth_date',)
    class Meta:
        model = Profile
admin.site.register(Profile, ProfileAdmin)

# admin.site.register(save_user_profile)